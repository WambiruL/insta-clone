from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url('search/', views.search_profile, name='search'),
]