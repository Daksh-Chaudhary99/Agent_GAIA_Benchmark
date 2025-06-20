import os
import base64
from llama_index.core.tools import FunctionTool
from llama_index.readers.file.image import ImageReader
from agent_models.models import get_vision_model_client
from agent_prompts.SystemPrompt import vision_model_system_prompt

def get_image_description(image_path: str) -> str:
    """
    Analyzes a local image and returns a text description. This tool is used to "see" what is in an image file.
    Args:
        image_path (str): The local file path of the image to analyze.
    """
    try:
        print(f"Analyzing image at path: {image_path}")

        # Read and encode the image
        with open(image_path, "rb") as img_file:
            b64_image = base64.b64encode(img_file.read()).decode("utf-8")
        b64_url = f"data:image/png;base64,{b64_image}"

        # Get Nebius client
        client = get_vision_model_client()

        # Call Nebius API
        response = client.chat.completions.create(
            model="Qwen/Qwen2-VL-72B-Instruct", 
            messages=[
                {
                    "role": "system",
                    "content": vision_model_system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Here is an image."},
                        {"type": "image_url", "image_url": {"url": b64_url}}
                    ]
                }
            ]
        )

        description = response.choices[0].message.content
        print(f"Vision model response: {description}")
        return description

    except Exception as e:
        return f"Error analyzing image: {e}"

# Wrapper function to create the tool for our agent
def get_image_interpreter_tool() -> FunctionTool:
    return FunctionTool.from_defaults(
        fn=get_image_description,
        name="image_interpreter",
        description="A tool to analyze an image from a local file path and return a detailed text description. Use this to 'see' what is in an image file that has already been downloaded."
    )