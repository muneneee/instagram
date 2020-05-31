from django.urls import path
from .views import PostView,DetailView
from .import views
from django.contrib.auth.views import LoginView


urlpatterns=[
    path('', PostView.as_view(),name = 'index'),
    path('profile/',views.profile, name='profile'),
    path('post/<int:pk>/', DetailView.as_view(), name='detail'),
]