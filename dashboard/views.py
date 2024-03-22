from django.shortcuts import render, redirect
from urllib import request
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

from django.http import JsonResponse

# def index(request):
#     return render(request,'index.html')



from django.http import JsonResponse




import io

from django.http import JsonResponse

def generate_image(user_input):
    API_URL = "https://api-inference.huggingface.co/models/artificialguybr/3DRedmond-V1"
    headers = {"Authorization": "Bearer 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"}

    payload = {"inputs": user_input}
    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content

    image = Image.open(io.BytesIO(image_bytes))
    return image
    
    
    
    # # modification
    
    # image.save(f"{settings.MEDIA_ROOT}/generated_image.jpg")
    # context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}

    #         # Wait for 4 seconds after the image is saved
    

    # return render(request, 'index.html')



import os


import contextlib
import time



import json
from django.http import JsonResponse

def index(request):
   
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        action = request.POST.get('action')
        
        if user_input:
            if action == 'image':
               cache.clear()
               generate_image(user_input).save(f"{settings.MEDIA_ROOT}/generated_image.jpg")
              
               context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}
            #    Wait for 4 seconds after the image is saved
            #    with wait_for_4_seconds():
            #       pass
               return render(request, 'index.html',context)

            elif action == 'music':
                # music = generate_music(user_input)
                # Process and return music
                return JsonResponse({'result': 'Music generated successfully.'})
            else:
                return JsonResponse({'error': 'Invalid action.'}, status=400)
        else:
            return render(request, 'index.html')
        if os.path.exists(f"{settings.MEDIA_ROOT}/generated_image.jpg"):
            context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}
        else:
            context = {'generated_image': f'{settings.STATIC_URL}default_image.jpg'}
    return render(request, 'index.html')


# def index(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         if user_input:
#             image = generate_image(user_input)
#             image.save(f"{settings.MEDIA_ROOT}/generated_image.jpg")
#             context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}

            # # Wait for 4 seconds after the image is saved
            # with wait_for_4_seconds():
            #     pass

#             return render(request, 'index.html', context)
#         else:
#             return render(request, 'index.html', {'error': 'Please enter a valid search term.'})
#     else:
#         if os.path.exists(f"{settings.MEDIA_ROOT}/generated_image.jpg"):
#             context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}
#         else:
#             context = {'generated_image': f'{settings.STATIC_URL}default_image.jpg'}
#         return render(request, 'index.html', context)

# @contextlib.contextmanager
# def wait_for_4_seconds():
#     if os.path.exists(f"{settings.MEDIA_ROOT}/generated_image.jpg"):
#         yield
#         time.sleep(4)

# def index(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         if user_input:
#             image = generate_image(user_input)
#             image.save(f"{settings.MEDIA_ROOT}/generated_image.jpg")
#             context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}
#             return render(request, 'index.html', context)
#         else:
#             return render(request, 'index.html', {'error': 'Please enter a valid search term.'})
#     else:
#         if os.path.exists(f"{settings.MEDIA_ROOT}/generated_image.jpg"):
#             context = {'generated_image': f'{settings.MEDIA_URL}generated_image.jpg'}
#         else:
#             context = {'generated_image': f'{settings.STATIC_URL}default_image.jpg'}
#         return render(request, 'index.html', context)

