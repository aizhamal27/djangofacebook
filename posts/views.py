from django.shortcuts import render, redirect
from posts.models import Post, PostLike, PostComment
from django.db.models import Q 

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("?")
    if request.method == "POST":
        key = request.POST.get('key')
        posts = Post.objects.filter(Q(title__icontains = key) | Q(description__icontains = key))
    context = {
        'posts' : posts,
    }
    return render(request, 'index.html', context)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        if 'like' in request.POST:
            try:
                like = PostLike.objects.get(user = request.user, post = post)
                like.delete()
            except:
                PostLike.objects.create(user = request.user, post = post)
        if 'comment' in request.POST:
            text = request.POST.get('text')
            comment = PostComment.objects.create(user = request.user, post = post, text = text)
            return redirect('post/post_detail', post.id)
    context = {
        'post' : post,
    }
    return render(request, 'post/post_detail.html', context)

def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Post.objects.create(user = request.user, title = title, description = description, image = image)
        return redirect('index')
    return render(request, 'post/post_create.html')

def post_update(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Post.objects.get(id = id)
        post.title = title 
        post.description = description
        post.image = image 
        post.save()
        return redirect('post_detail', post.id)
    context = {
        'post' : post,
    }
    return render(request, 'post/post_update.html', context)

def post_delete(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('index')
    context = {
        'post' : post
    }
    return render(request, 'post/post_delete.html', context)