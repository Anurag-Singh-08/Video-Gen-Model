from generate_frames.py import generate_frames
from video_utils import make_video

prompt_path = "prompts/prompt.txt"
frames_dir = "frames"
video_output = "output.mp4"

prompt = open(prompt_path).read().strip()

generate_frames(prompt, frames_dir, num_frames=30)
make_video(frames_dir, video_output)
