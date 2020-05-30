from django.urls import path
from .import views
from django.contrib.auth.views import LoginView


urlpatterns=[
    path('', views.index,name = 'index'),
    path('profile',views.profile, name='profile')
]