from django.shortcuts import render, get_object_or_404
from .models import Image, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import ImageForm, CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ImageForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'index.html', params)

def search(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        search_term = request.GET.get("search_user")
        searched_profile = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message, "profile":searched_profile})
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html', {'message': message})

def profile(request):
    current_user = request.user
    images =  Image.objects.filter(profile = current_user.profile)
    try:
        profile = Profile.objects.get(user = current_user)
        
    except: 
        ObjectDoesNotExist
    print(profile.bio)
    
    context = {
        
        'profile':profile,
        'images':images,
        'current_user':current_user
    }
        
    return render(request,'profile.html', context)

def post_comment(request, id):
    image = get_object_or_404(Image, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    params = {
        'image': image,
        'form': form,
    }
    return render(request, 'single_image.html', params)


