import cv2
import os

def make_video(frame_dir, output_path, fps=15):
    frames = sorted([f for f in os.listdir(frame_dir) if f.endswith(".png")])
    if len(frames) == 0:
        raise ValueError("No frames found!")

    img = cv2.imread(os.path.join(frame_dir, frames[0]))
    height, width, _ = img.shape

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for frame in frames:
        img = cv2.imread(os.path.join(frame_dir, frame))
        video.write(img)

    video.release()
    print("Video saved:", output_path)
