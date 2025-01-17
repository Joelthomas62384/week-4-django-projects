from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url="login")
def home(request):
    return render(request, "index.html")


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"User login successfull")
            return redirect("home")
        
        else:
            messages.error(request,"Invalid username or password")

    
    return render(request,"login.html")

def Signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confpass = request.POST.get('confirmpassword')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('signup')

        if password != confpass:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Your account has been created successfully. Please log in.')
        return redirect('login')

    return render(request, "signup.html")

def Logout(request):
    logout(request)
    messages.success(request,"Logout Successfull")
    return redirect('login')





