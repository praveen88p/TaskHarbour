import json
from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from urllib3 import request

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

import subprocess



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

def upsc_img(request):
        if request.method == 'POST' and request.FILES['image']:
            image_file = request.FILES['image']

            # Save the uploaded file to the current directory
            with open(image_file.name, 'wb+') as destination:
               for chunk in image_file.chunks():
                    destination.write(chunk)

            return JsonResponse({'message': 'Image uploaded successfully.'})
        else:
            return  render(request, 'img_upsc.html')


        




# read me generaion





# def gen_readme(request):
    
#     return render(request, 'readme_gen.html')

import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyCONZqruFjhIRhyZE8UH2CUOQH9eeCn5bE")

# Initialize the generative model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def gen_readme(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input.lower() == 'exit':
            return JsonResponse({'response': 'Conversation ended.'})

        # Start the chat with the user input as history
        convo = model.start_chat(history=[])
       
      
        # Send user message and retrieve response from the model
        response = convo.send_message(f"Create a Readme file for my code : {user_input}")
        generated_response = response.candidates[0].content.parts[0].text
        generated_response = generated_response.replace('#', '\n \n')
        generated_response = generated_response.replace('*', '\n \n')
        generated_response = generated_response.replace('.', '\n \n')
          # End the conversation
        context ={
           
            'generated_response': generated_response,
            }
        return render(request, 'readme_gen.html', context)
        
    
    return render(request, 'readme_gen.html')



########################################################################################################################        
#ERROR Solver 

import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyCONZqruFjhIRhyZE8UH2CUOQH9eeCn5bE")

# Initialize the generative model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def sol_error(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input.lower() == 'exit':
            return JsonResponse({'response': 'Conversation ended.'})

        # Start the chat with the user input as history
        convo = model.start_chat(history=[])
       
      
        # Send user message and retrieve response from the model
        response = convo.send_message(f"solve error in the code : {user_input}")
        generated_response2 = response.candidates[0].content.parts[0].text
       
          # End the conversation
        context ={
           
            'generated_response2': generated_response2,
            }
        return render(request, 'error_sol.html', context)
        
    
    return render(request, 'error_sol.html')


    



