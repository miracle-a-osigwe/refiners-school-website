from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin interface to control the posting of document based on user privileges.
    """
    model = Post
    list_display = ['title', 'content', 'img', 'url']