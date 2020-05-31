from django.urls import path
from .views import PostView,DetailView,CreateView
from .import views


urlpatterns=[
    path('', PostView.as_view(),name = 'index'),
    path('profile/',views.profile, name='profile'),
    path('post/<int:pk>/', DetailView.as_view(), name='detail'),
    path('post/new/', CreateView.as_view(), name='create'),

]