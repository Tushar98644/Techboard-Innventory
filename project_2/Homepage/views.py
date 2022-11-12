from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    return render(request,'index.html');

def aboutus(request):
    return render(request,'Aboutus.html');  

def book(request):
    return render(request,'book.html');      