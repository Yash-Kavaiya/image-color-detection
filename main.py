import gradio as gr
import numpy as np
from PIL import Image

def generate_image(noise_level):
    """
    This function generates a sample image. You'll likely replace this with
    your actual image generation logic (e.g., loading a model).

    Args:
       noise_level (float): A value between 0 and 1 controlling the 
                            amount of noise to add to the image.  

    Returns:
       A PIL Image object.
    """
    width, height = 256, 256  # Customize image dimensions as needed
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)  # Random noise
    data = data * noise_level
    img = Image.fromarray(data)
    return img

# Build the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Slider(0, 1, step=0.05, label="Noise Level"),
    outputs="image",
    title="My Projects",
    description="Experiment with generating images by adjusting the noise level."
)

iface.launch() 
