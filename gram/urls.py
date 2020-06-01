from django.urls import path
from .views import PostView#,DetailView,CreateView,UpdatePostView,DeletePostView,ProfileFollowToggle
from .import views


urlpatterns=[
    path('', PostView.as_view(),name = 'index'),
    # path('profile/',views.profile, name='profile'),
    # path('like/',views.like_post, name='like-post'),
    # path('follow/',ProfileFollowToggle.as_view(), name='follow'),
    # path('post/<int:pk>/', DetailView.as_view(), name='detail'),
    # path('post/(?P<id>\d+)/comment/', views.add_comment, name='comment'),
    # path('post/new/', CreateView.as_view(), name='create'),
    # path('post/<int:pk>/update/', UpdatePostView.as_view(), name='update'),
    # path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete'),

]