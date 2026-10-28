from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post

def home(request):
    posts= Post.objects.order_by("?")[:10]
    return render(request, "home.html",{
        "posts": posts
    })
  
@login_required    
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        
        if content:
            Post.objects.create(content=content, user=request.user)
            return redirect("home")
        
    return render(request, "create_post.html")

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    
    if request.method =="POST":
        content = request.POST.get("content","").strip()
        
        if content:
            post.content =content
            post.save()
            return redirect ("home")
        
    return render(request, "edit_post.html", {"post":post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return redirect("home")
