import base64
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


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
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    response = client.chat.completions.create(
        max_tokens = 16000,
        model = 'gpt-4o-mini',
        messages = [
            {
                "role" : "system",
                "content" : f"{instruction_prompt}"
            },
            {
                "role" : "user",
                "content" : [
                    {"type" : "text", "text" : f"{user_prompt}"},
                    *[
                        {
                            "type" : "image_url" , "image_url" : {
                                "url" : f"data:image/png;base64,{base64_image}"
                            }
                        }
                        for base64_image in base64_images
                    ]
                ]
            }
        ]
    )

    print(response.choices[0].message.content)
    trim_response = response.choices[0].message.content.replace('``markdown',"").replace('```',"")
    with open('response_markdown.md','w') as f:
        f.write(trim_response)

    