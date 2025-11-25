from diffusers import StableDiffusionPipeline
import torch
import os

def generate_frames(prompt, output_dir, num_frames=30):
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    ).to("cuda")

    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_frames):
        print(f"Generating frame {i+1}/{num_frames}")
        image = pipe(prompt).images[0]
        image.save(f"{output_dir}/frame_{i:03d}.png")
