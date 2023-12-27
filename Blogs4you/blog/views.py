from django.shortcuts import render
from .models import Category, Post

# Create your views here.

def index(request):
    c = Category.objects.all()[:6]
    posts = Post.objects.all()[:4]
    return render(request, 'index.html',
                  {
                      'categories':c,
                      'posts':posts
                  })
