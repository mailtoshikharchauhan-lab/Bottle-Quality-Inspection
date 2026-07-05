import cv2
import os
from glob import glob

# -----------------------------
# Image Folder
# -----------------------------
image_folder = "dataset"

# -----------------------------
# Output Video
# -----------------------------
output_video = "videos/input.mp4"

# Create videos folder
os.makedirs("videos", exist_ok=True)

# -----------------------------
# Read Images
# -----------------------------
image_paths = sorted(glob(os.path.join(image_folder, "*.jpg")))

print(f"Total Images: {len(image_paths)}")

if len(image_paths) == 0:
    raise Exception("No images found!")

# -----------------------------
# Read First Image
# -----------------------------
first = cv2.imread(image_paths[0])

height, width = first.shape[:2]

# -----------------------------
# Video Writer
# -----------------------------
fps = 10  # 10 images per second

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

# -----------------------------
# Write Frames
# -----------------------------
for img_path in image_paths:

    frame = cv2.imread(img_path)

    video.write(frame)

video.release()

print("Video Created Successfully!")
print(output_video)