from django.shortcuts import render, redirect
from videos.models import Video, VideoLike, VideoComment

# Create your views here.
def index_video(request):
    videos = Video.objects.all().order_by('?')
    context = {
        'videos' : videos,
    }
    return render(request, 'video/video.html', context)

def video_detail(request, id):
    video = Video.objects.get(id = id)
    if request.method == "POST":
        if 'like' in request.POST:
            try:
                like = VideoLike.objects.get(user = request.user, video = video)
                like.delete()
            except:
                VideoLike.objects.create(user = request.user, video = video)
        if 'comment' in request.POST:
            text = request.POST.get('text')
            comment = VideoComment.objects.create(user = request.user, video = video, text = text)
            return redirect('video_detail', video.id)

    context = {
        'video' : video
    }
    return render(request, 'video/video_detail.html', context)

def create_video(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        video = request.FILES.get('video')
        Video.objects.create(user = request.user, title = title, description = description, video_file = video)
        return redirect('index_video')

    return render(request, 'video/create_video.html')

def update_video(request, id):
    video = Video.objects.get(id = id)
    if request.method == "POST":
        title_video = request.POST.get('title')
        description = request.POST.get('description')
        video = Video.objects.get(id = id)
        video.title = title_video
        video.description = description
        video.save()
        return redirect('video_detail', video.id)
    context = {
        'video' : video
    }
    return render(request, 'video/update_video.html', context)

def delete_video(request, id):
    video = Video.objects.get(id = id)
    if request.method == "POST":
        video = Video.objects.get(id = id)
        video.delete()
        return redirect('index_video')
    context = {
        'video' : video
    }
    return render(request, 'video/delete_video.html', context)