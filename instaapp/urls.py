from . import views
from django.conf.urls import url, include

urlpatterns=[
    url(r'register/', views.registerPage, name='register'),
    url(r'login/', views.LoginPage, name='login'),
    url(r'account/', include('django.contrib.auth.urls')),
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/<username>/', views.profile, name='profile'),
    url(r'^images/(?P<id>\d+)/comment', views.post_comment, name = 'post_comment'),
    url(r'^like', views.like_post, name='like_post'),
   
]