from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from .forms import AddPostForm


def homepage(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/homepage.html", context)


def post_details(request, slug):
    post = Post.objects.filter(slug=slug)

    if post.exists():
        post = post[0]
    else:
        return HttpResponse("Page not found")

    context = {"post": post}
    return render(request, "blog/post_details.html", context)


def create_post(request):
    form = AddPostForm()

    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            created_post = form.save(commit=False)
            created_post.user = request.user
            created_post.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "blog/add_post.html", context)


def delete_post(request, slug):
    post = Post.objects.filter(slug=slug)[0]

    if request.method == "POST":
        post.delete()
        return redirect("/")
    context = {"post": post}

    return render(request, "blog/delete_post.html", context)


def edit_post(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    form = AddPostForm(instance=post)

    if request.method == "POST":
        form = AddPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "blog/add_post.html", context)
