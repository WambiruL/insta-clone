from django.shortcuts import render
from .models import Image, Profile


# Create your views here.
def index(request):
    images=Image.retrieve_images()
   
    params = {
        'images': images,
    }
    return render(request, 'home.html', params)


def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})