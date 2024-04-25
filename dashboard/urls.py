from django.urls import path
from . import views




urlpatterns = [
    path('', views.index_blank, name='index'),

    path('index_link', views.index, name='index'),

    path('image_link', views.gen_image, name ='image-generator'),

    path('music_link', views.gen_music, name ='music-generator'),

    path('readme_link', views.gen_readme, name ='readme-generator'),

    path('error-sol_link', views.sol_error, name ='error-solver'),

    path('image-upscale_link', views.upsc_img, name ='image-upscale')

]