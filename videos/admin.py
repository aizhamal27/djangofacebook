from django.contrib import admin
from videos.models import Video, VideoLike, VideoComment

# Register your models here.
admin.site.register(Video)
admin.site.register(VideoLike)
admin.site.register(VideoComment)