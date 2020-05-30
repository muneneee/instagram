from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Image



def index(request):

    photos = Image.objects.all()

    return render(request, 'insta/index.html', {'photos':photos})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})