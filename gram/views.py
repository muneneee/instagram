from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image



def index(request):

    photos = Image.objects.all()

    return render(request, 'insta/index.html', {'photos':photos})
