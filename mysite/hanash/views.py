from django.shortcuts import render,redirect,get_object_or_404
from .models import HanashUser
from django.contrib import messages
from .models import Message,Room,Comments,Posts
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.
def LikeView(request,pk):
    print(pk)
    huser=HanashUser.objects.filter(user=request.user)
    post=get_object_or_404(Posts,id=pk)
    cu_lc=post.likes_count+1
    post.likes.add(huser[0])
    post.likes_count=cu_lc
    post.save()
    return redirect('/hanash/newsfeed/')
def index(request):
    return render(request, 'index.html',{})

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password!=cpassword:
            messages.error(request,"password doesn't match")
        else:
            us=User.objects.create(first_name=first_name,email=email,username=username,last_name=last_name,password=password)
            us.save()
            contact=HanashUser.objects.create(user=us,phone=phone)
            contact.save()
            messages.success(request,'Data has been submitted')
    return render(request,'register.html')
def loginus(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            
        else:
            messages.info(request,"username or password is incorrect")
    return render(request,'login.html')

@login_required(login_url='/hanash/login/')
def room(request,room_name):
    username = request.user.username
    print(username)
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'room.html', {'room_name': room_name,'username': username, 'messages': messages})
    
@login_required(login_url='hanash/login/')
def newsfeed(request):
    posts=Posts.objects.all().order_by('-date_created')
    #return render(request,'newsfeed.html')
    return render(request,'newsfeed.html',context={'posts':posts})
    
