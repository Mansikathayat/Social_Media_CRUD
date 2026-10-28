from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists."})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return render(request, "signup.html", {
            "success": "Account created successfully!"})
        
    return render(request, "signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        return render(request, "login.html",{
            "error": "Invalid username or password."
        })
        
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")