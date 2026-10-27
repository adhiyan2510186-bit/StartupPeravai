"""
People counter using YOLOv8.

Usage:
    python counter.py TestVideo1.mp4

Press "q" in the video window to quit.
"""

import sys
import time
from collections import deque

import cv2
from ultralytics import YOLO

# ---------------------------------------------------------------
# Settings you can tweak
# ---------------------------------------------------------------
MODEL_FILE = "yolov8n.pt"   # "n" = nano, the smallest/fastest model. Downloads automatically the first time.
PERSON_CLASS = 0            # In YOLO's COCO dataset, class 0 is "person"
CONFIDENCE = 0.4            # Ignore detections YOLO is less than 40% sure about
AVERAGE_SECONDS = 3         # Smooth the count over this many seconds of video
DISPLAY_WIDTH = 960         # Shrink big videos so the window fits on screen

# ---------------------------------------------------------------
# 1. Read the video file name from the command line
# ---------------------------------------------------------------
if len(sys.argv) < 2:
    print("Please give a video file, e.g.:  python counter.py TestVideo1.mp4")
    sys.exit(1)

video_path = sys.argv[1]

# ---------------------------------------------------------------
# 2. Open the video and load the YOLO model
# ---------------------------------------------------------------
video = cv2.VideoCapture(video_path)
if not video.isOpened():
    print(f"Could not open video: {video_path}")
    sys.exit(1)

model = YOLO(MODEL_FILE)

# Find out how many frames per second the video has (fall back to 30 if unknown)
fps = video.get(cv2.CAP_PROP_FPS) or 30

# A deque is a list with a maximum length: when it is full, adding a new
# item automatically drops the oldest one. We keep the person count of the
# last few seconds of frames here, then average them.
recent_counts = deque(maxlen=int(fps * AVERAGE_SECONDS))

last_print_time = time.time()

# ---------------------------------------------------------------
# 3. Process the video one frame at a time
# ---------------------------------------------------------------
while True:
    ok, frame = video.read()
    if not ok:
        break  # End of the video

    # Run YOLO on this frame, asking it to look for people only
    results = model(frame, classes=[PERSON_CLASS], conf=CONFIDENCE, verbose=False)
    boxes = results[0].boxes

    # Draw a green box around each person
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Count people in this frame, then average over the recent frames
    recent_counts.append(len(boxes))
    average_count = round(sum(recent_counts) / len(recent_counts))

    # Write the smoothed count in the top-left corner (black outline + white text)
    label = f"People: {average_count}"
    cv2.putText(frame, label, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 8)
    cv2.putText(frame, label, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 3)

    # Print the count to the terminal once per second
    now = time.time()
    if now - last_print_time >= 1:
        print(f"People in view: {average_count}")
        last_print_time = now

    # Shrink the frame if it is wider than DISPLAY_WIDTH, then show it
    height, width = frame.shape[:2]
    if width > DISPLAY_WIDTH:
        scale = DISPLAY_WIDTH / width
        frame = cv2.resize(frame, (DISPLAY_WIDTH, int(height * scale)))
    cv2.imshow("People Counter", frame)

    # Wait 1 ms for a key press; quit if it is "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ---------------------------------------------------------------
# 4. Clean up
# ---------------------------------------------------------------
video.release()
cv2.destroyAllWindows()
print("Done.")
