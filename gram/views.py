from django.shortcuts import render,redirect
from django.http import HttpResponse
from django .contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image
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
            messages.success(request, f'Account {username} created')
            return redirect('login_url')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html',{'form':form})


def profile(request):
    return render(request, 'insta/profile.html')