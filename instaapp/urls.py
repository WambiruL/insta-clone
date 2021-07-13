from . import views
from django.conf.urls import url, include
from instaapp import views as instaapp_views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'register/', instaapp_views.registerPage, name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'logout/',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/<username>/', views.profile, name='profile'),
    url(r'user_profile/<username>/', views.user_profile, name='user_profile'),
    url(r'^images/(?P<id>\d+)/comment', views.post_comment, name = 'post_comment'),
    url(r'^like', views.like_post, name='like_post'),
    url(r'unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url(r'follow/<to_follow>', views.follow, name='follow')
   
]