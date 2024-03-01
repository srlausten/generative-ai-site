from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
from PIL import Image
import base64
from io import BytesIO

def generate_image(prompt):
    model_id = "stabilityai/stable-diffusion-2"
    
    # Initialize the Euler scheduler
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    
    # Load the pipeline with the specified scheduler and set the precision
    pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float32).to("cpu")
    
    print('Model Loaded...')
    # Generate the image
    result = pipe(prompt)
    image = result.images[0]
    print('Success Image Generated!')
    
    # Convert the image to a base64 string for HTML embedding
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return f"data:image/png;base64,{img_str}"

