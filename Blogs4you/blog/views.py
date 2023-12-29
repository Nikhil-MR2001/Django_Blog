from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm
from .models import Category, Post
from django.contrib.auth import login as auth_login  # Alias the login function


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    c = Category.objects.all()[:6]
    posts = Post.objects.all().order_by('-created')[:3]
    return render(request, 'index.html',
                  {
                      'categories': c,
                      'posts': posts
                  })


def blog_detail(request, post_id):
    blog_post = get_object_or_404(Post, post_id=post_id)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})


def allblog(request):
    blogs = Post.objects.all()[:6]
    return render(request, 'all.html', {'blogs': blogs})


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # Log in the user after registration
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            # Redirect to a success page or home page
            return redirect('index/')
        else:
            # Handle form errors if needed
            pass
    else:
        user_form = UserForm()

    return render(request, 'signup.html', {'user_form': user_form})


def login(request):
    if request.method == 'POST':
        # Retrieve the values from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform custom authentication (replace this with your actual authentication logic)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            auth_login(request, user)
            # Redirect to a success page or home page
            return redirect('index')
        else:
            # Handle authentication failure (e.g., display an error message)
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
