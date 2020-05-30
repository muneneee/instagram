from django.shortcuts import render,redirect
from django.http import HttpResponse
from django .contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image
from django.contrib.auth.models import User
from .email import send_welcome_email
from .forms import RegisterForm


@login_required
def index(request):

    photos = Image.objects.all()

    return render(request, 'insta/index.html', {'photos':photos})


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


def profile(request):
    return render(request, 'insta/profile.html')