from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.startpage, name="startpage"),
    path("posts/", views.posts, name="post_list"),
    path("me/", views.about_me, name="about_me"),
    path("post/<int:pk>/", views.post, name="post_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)