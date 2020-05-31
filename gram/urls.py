from django.urls import path
from .views import PostView
from .import views
from django.contrib.auth.views import LoginView


urlpatterns=[
    path('', PostView.as_view(),name = 'index'),
    path('profile',views.profile, name='profile')
]