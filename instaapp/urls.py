from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/<username>/', views.profile, name='profile'),
    url(r'^images/(?P<id>\d+)/comment', views.post_comment, name = 'post_comment'),
   
]