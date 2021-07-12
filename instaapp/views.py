from django.shortcuts import redirect, render, get_object_or_404
from .models import Image, Profile, Follow
from django.contrib.auth.models import User
from .forms import ImageForm, CommentForm, UserUpdateForm,ProfleUpdateForm, CreateUserForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist



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

@login_required(login_url='/login')
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


def user_profile(request):
    current_user = request.user
   
    # image =  Image.objects.all()
    try:
        profile = Profile.objects.get(user=current_user)
        
    except: 
        ObjectDoesNotExist
    print(profile.bio)
    
    context = {
        
        'profile':profile,
        
        'current_user':current_user
    }
        
    return render(request,'users_profile.html', context)

class AppListView(ListView):
    model = Image
    template_name = 'index.html' 

def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('user_profile', user_profile2.user.username)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('user_profile', user_profile3.user.username)

