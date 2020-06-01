from django.shortcuts import render,redirect,get_object_or_404
from django .contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image,Profile,Comment,Like
from django.contrib.auth.models import User
from .email import send_welcome_email
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .forms import RegisterForm,ProfileForm,UpdateForm,CommentForm



@login_required
def index(request):

    posts = Image.objects.all()

    return render(request, 'insta/index.html', {'posts':posts},{'users':users})


def navbar(request):

    users = User.objects.all()

    return render(request, 'sidenav.html',{'users':users})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            send_welcome_email(username,email)

            messages.success(request, f'Account {username} created')
            return redirect('login')
    else:
        form = RegisterForm()
        
    
    return render(request, 'registration/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account {username} has been updated')
            return redirect('profile')

    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {'user_form':user_form, 'profile_form':profile_form}


    return render(request, 'insta/profile.html', context)

@login_required
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Image.objects.get(id = post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'like'

        like.save()
    

    return redirect('index')



class PostView(ListView):
    model = Image
    template_name = 'insta/index.html'
    context_object_name = 'posts'
    ordering = ['-posted']


class DetailView(DetailView):
    model = Image
    template_name = 'insta/detail.html'
    
    

class CommentCreate(LoginRequiredMixin,CreateView):
    model= Comment
    template_name = 'insta/comment_form.html'
    success_url = '/'
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post =self.request.POST.get('post_id')
        #form.instance.post = get_object_or_404(Image, pk=image_id)
        return super().form_valid(form)


class CreateView(LoginRequiredMixin,CreateView):
    image = ImageField(label='post')

    model = Image
    success_url = '/'
    template_name = 'insta/post_form.html'
    fields = [ 'name', 'caption','image']


    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    image = ImageField(label='post')

    model = Image
    success_url = '/'
    template_name = 'insta/post_form.html'
    fields = [ 'name', 'caption','image']


    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.account:
            return True
        return False



class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Image
    
    success_url = '/'
    template_name = 'insta/post_delete.html'

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.account:
            return True
        return False


class ProfileFollowToggle(LoginRequiredMixin,View):
    template_name = 'insta/profile.html'

    def post(self, request, *args, **kwargs):
        return redirect ('index')
