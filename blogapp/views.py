from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import BlogPost
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        unm = request.POST.get('unm')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        my_user = User.objects.create_user(username=unm,email=email,password=pwd)
        my_user.save()
        return redirect('loginn')
    return render(request,'signup.html')

def loginn(request):
    if request.method == 'POST':
        unm = request.POST.get('unm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request,username=unm,password=pwd)
        print(unm)
        print(pwd)
        print(userr)
        if userr is not None:
            login(request,userr)
            return redirect('posts')
        else:
            print("Wrong Credentials")
            return HttpResponse("<h1>Wrong Credentials</h1>")
    return render(request,'user_login.html')

def index(request):
    return render(request,'index.html')

#ALL POSTS
@login_required
def posts(request):
    Postss = BlogPost.objects.all()
    context = {
        'posts' : Postss
    }
    return render(request,'posts.html',context)

@login_required
def mypost(request):
    myposts = BlogPost.objects.filter(author=request.user)
    context = {
        'posts' : myposts
    }
    return render(request,'myposts.html',context)

@login_required
def createpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        user = request.user
        print(user)
        BlogPost.objects.create(title=title,author=user,desc=desc)
        return redirect('posts')
    return render(request,'newpost.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('loginn')