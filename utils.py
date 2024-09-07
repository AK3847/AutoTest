import base64
from typing import List

def convert_image(image_path: str):
    base64_string = ""
    with open(image_path,'rb') as f:
        base64_string = base64.b64encode(f.read()).decode('utf-8')
    return base64_string


def generate_response(image_paths: List[str], user_prompt: str = ""):

    base64_images = [convert_image(x) for x in image_paths]

    instruction_prompt = ""
    with open('instruction_prompt.txt','r',encoding="utf8") as f:
        instruction_prompt = f.read()
    
    