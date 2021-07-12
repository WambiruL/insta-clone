import re
from django.shortcuts import redirect, render, get_object_or_404
from .models import Image, Profile
from django.contrib.auth.models import User
from .forms import ImageForm, CommentForm, UserUpdateForm,ProfleUpdateForm, CreateUserForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string


# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context={'form':form}
    return render(request, 'registration/registration_form.html',context)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,username)
        return redirect('index')

    context={}
    return render(request, 'registration/login.html',context)

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
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfleUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfleUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
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

def like_post(request):
    image = get_object_or_404(Image, id=request.POST.get('id'))
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked = False

    params = {
        'image': image,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    if request.is_ajax():
        html = render_to_string('like_post.html', params, request=request)
        return JsonResponse({'form': html})


