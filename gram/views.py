from django.shortcuts import render,redirect
from django .contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image,Profile
from django.contrib.auth.models import User
from .email import send_welcome_email
from pyuploadcare.dj.forms import ImageField
from django.views.generic import ListView,DetailView,CreateView
from .forms import RegisterForm,ProfileForm,UpdateForm


@login_required
def index(request):

    posts = Image.objects.all()

    return render(request, 'insta/index.html', {'posts':posts})



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



class PostView(ListView):
    model = Image
    template_name = 'insta/index.html'
    context_object_name = 'posts'
    ordering = ['-posted']


class DetailView(DetailView):
    model = Image
    template_name = 'insta/detail.html'


class CreateView(CreateView):
    image = ImageField(label='post')

    model = Image
    success_url = '/'
    template_name = 'insta/post_form.html'
    fields = [ 'name', 'caption','image']


    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


