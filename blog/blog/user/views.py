from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from . models import Userdb, Post
from . forms import userform, postform


# Create your views here.
def page(request,pval):
    allPosts=Post.objects.filter(categoryid=pval)
    context = {'allPosts': allPosts}
    return render(request,'page.html',context)

def dashboard(request):
    if request.method=='POST':
        form=postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=postform()
    allPosts = Post.objects.all()
    contex={'postform':form,'allposts':allPosts}
    return render(request,'dashboard.html',contex)

def home(request):
    allPosts = Post.objects.all()[:5]
    context = {'allPosts': allPosts}
    return render(request, "home.html", context)

def blogpost(request, slug):
   if Post.objects.filter(slug=slug).first():
    post=Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, "post.html", context)
   else:
       return HttpResponse("<h1>page not found</h1>")

def handelLogout(request):
    logout(request)
    print("----------------------")
    return redirect('home')

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return redirect("home")

    return HttpResponse("404- Not found")
