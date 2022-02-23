from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import ListView
import uuid
import boto3


# S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
# BUCKET = 'photodeck'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

class PostCreate(CreateView):
    model = Post
    fields = ('title', 'description',)