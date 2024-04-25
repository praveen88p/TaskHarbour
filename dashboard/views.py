import json
from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from urllib3 import request
import openai
import requests
from django.http import JsonResponse
import random
import os
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.cache import cache
from PIL import Image
import io
import os
import contextlib
import time
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()



def index_blank(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')


# FOR IMAGE GENERATION
def generated_image(user_input):
    API_URL = "https://api-inference.huggingface.co/models/artificialguybr/3DRedmond-V1"
    headers = {"Authorization": "Bearer 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"}

    payload = {"inputs": user_input}
    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content

    image = Image.open(io.BytesIO(image_bytes))
    cache.clear()
    return image
        
def gen_image(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        generated_image(user_input).save(f"{settings.MEDIA_ROOT}/generated_image.jpg")

        context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}
      
        return render(request, 'image_gen.html', context)
    else:
        return render(request, 'image_gen.html')
 



# FOR MUSIC GENERATION
    

def generate_music(user_input):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer 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"}

    payload = {"inputs": user_input}
    response = requests.post(API_URL, headers=headers, json=payload)
    audio_bytes= response.content   
    return audio_bytes    

def gen_music(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        audio_bytes = generate_music(user_input)
        audio_file = BytesIO(audio_bytes)
        audio_file.name = "generated_music.mp3"
        with open(f"{settings.MEDIA_ROOT}/generated_music.mp3", "wb") as f:
            f.write(audio_file.read())
        context = {'generated_image': f'{settings.MEDIA_URL}generated_music.mp3'}
        return render(request,'music_gen.html',context)
    return render(request, 'music_gen.html')



# for upscaling\


import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "r8_enOV1KZHibj3kWt5nVd0jwCgw2rTQXV0LPLUH"


def upsc_img(request):
    if request.method == "POST":
        # Get the image file from the request
        image_file = request.FILES["image"]

        # Call the API with the image file
        input = {"img": image_file}
        output =replicate.run("tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c", input)

        # Render the output in the HTML template
        return render(request, "img_upsc.html", {"output": output})

    return render(request, "img_upsc.html")


# read me generaion

def extract_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"

api_key = os.getenv('OPENAI_KEY',None)
def gen_readme(request):
    if request.method == 'POST':
        file_path = request.POST.get('fileInput')  # Assuming you're sending the file path in a POST request
        if file_path:
            file_contents = extract_file_contents(file_path)
            openai.api_key = api_key
            # Send the contents of the code file to the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Generate a README file for the following Python code: ```{file_contents}```"}
                ]
            )
            generated_readme = response.choices[0].message.content
            context = {
                'generated_readme_content': generated_readme,
                'generated_readme_name': 'README.md'
            }

            return render(request, 'readme_gen.html', context)
         

    return render(request, 'readme_gen.html')
    
     

        

        

 
    return render(request, 'readme_gen.html')


def sol_error(request):
    return render(request,'error_sol.html')

