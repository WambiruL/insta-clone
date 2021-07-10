from django.shortcuts import render
from .models import Image


# Create your views here.
def index(request):
    images=Image.retrieve_images()
   
    params = {
        'images': images,

    }
    return render(request, 'index.html', params)

