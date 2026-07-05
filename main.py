import cv2
import time
import os

from detector import BottleDetector
from utils import UI

# ==========================================================
# PATHS
# ==========================================================

MODEL_PATH = "models/best.pt"

INPUT_VIDEO = "videos/input.mp4"

OUTPUT_VIDEO = "output/output.mp4"

# ==========================================================
# LOAD MODEL
# ==========================================================

detector = BottleDetector(MODEL_PATH)

# ==========================================================
# LOAD UI
# ==========================================================

ui = UI()

# ==========================================================
# VIDEO
# ==========================================================

cap = cv2.VideoCapture(INPUT_VIDEO)

if not cap.isOpened():

    print("Cannot open video!")

    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps_video = cap.get(cv2.CAP_PROP_FPS)

os.makedirs("output", exist_ok=True)

writer = cv2.VideoWriter(

    OUTPUT_VIDEO,

    cv2.VideoWriter_fourcc(*'mp4v'),

    fps_video,

    (width, height)

)

# ==========================================================
# WINDOW
# ==========================================================

cv2.namedWindow(

    "Bottle Quality Inspection",

    cv2.WINDOW_NORMAL

)

cv2.resizeWindow(

    "Bottle Quality Inspection",

    1500,

    900

)

# ==========================================================
# FPS
# ==========================================================

prev_time = time.time()

frame_no = 0

# ==========================================================
# LOOP
# ==========================================================

while True:

    success, frame = cap.read()

    if not success:

        break

    frame_no += 1

    detections = detector.detect(frame)

    detected = len(detections)

    passed = 0

    failed = 0

    # --------------------------------------

    for detection in detections:

        status = ui.draw_detection(frame, detection)

        if status == "PASS":

            passed += 1

        else:

            failed += 1

    # --------------------------------------

    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # --------------------------------------

    ui.draw_dashboard(

        frame,

        frame_no,

        fps,

        detected,

        passed,

        failed

    )

    # --------------------------------------

    writer.write(frame)

    cv2.imshow(

        "Bottle Quality Inspection",

        frame

    )

    key = cv2.waitKey(1)

    if key == 27:

        break

# ==========================================================
# CLEANUP
# ==========================================================

cap.release()

writer.release()

cv2.destroyAllWindows()

print("=" * 60)

print("Processing Finished")

print()

print("Output Saved To")

print(OUTPUT_VIDEO)

print("=" * 60)