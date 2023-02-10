# This is specifically for use with gui.py. Do not modify.

import requests
import openai
moderation_endpoint_url = "https://api.openai.com/v1/moderations"

def get_moderation_response(input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }
    data = {"input": f"{input}"}
    response = requests.post(moderation_endpoint_url, headers=headers, json=data)
    response_data = response.json()
    return response_data['results'][0]['flagged']

def get_filter_response(input):
    response = openai.Completion.create(
        model="content-filter-alpha",
        prompt = f"<|endoftext|>{input}\n--\nLabel:", # This format is required, do not change
        temperature=0, # Doesn't need to be modified
        max_tokens=1, # Doesn't need to be modified - only returns a single integer
        top_p=0, # See docs for explanation
        logprobs=10 # See docs for explanation
    )

    return response.choices[0].text

def get_gpt_response(input, model, key):
    openai.api_key = key.strip()
    response = openai.Completion.create(
    model=model, # Other models available which may be cheaper, see docs for more information
    prompt=input,
    max_tokens=800, # Max tokens allowed - up to 4000 for Davinci, see docs for more information
    temperature=0.5, # See docs for explanation
    )
    return response.choices[0].text

# 
def get_img_response(input):
    response = openai.Image.create(
            prompt = input,
            n=1, # Number of created images - up to 10
            size="1024x1024" # Image resolution - must be 1024x1024, 512x512, or 256x256 only
        )
    return response['data'][0]['url']