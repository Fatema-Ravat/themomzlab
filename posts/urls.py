from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.list_post,name='list_post'),
    path('create_post/',views.create_post,name='create_post'),
    
]