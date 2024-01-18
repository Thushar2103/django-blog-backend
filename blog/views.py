from django.shortcuts import render
from django.views.generic import UpdateView
from rest_framework import viewsets
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import *
from .serializer import *

# Create your views here.
class BlogpostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer

def home(request): 
    # return response 
    return render(request, "home.html") 