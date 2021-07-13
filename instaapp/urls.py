from . import views
from django.conf.urls import url, include

urlpatterns=[
   url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'register/', views.registerPage, name='register'),
    url(r'^$',views.index,name = 'index'),
    url(r'login/', views.LoginPage, name='login'), 
    
    
    url(r'^search/', views.search, name='search'),
    url(r'^profile/<username>/', views.profile, name='profile'),
    url(r'user_profile/<username>/', views.user_profile, name='user_profile'),
    url(r'^images/(?P<id>\d+)/comment', views.post_comment, name = 'post_comment'),
    url(r'^like', views.like_post, name='like_post'),
    url(r'unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url(r'follow/<to_follow>', views.follow, name='follow')
   
]