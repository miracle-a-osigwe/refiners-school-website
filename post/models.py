from django.db import models, connection

# Create your models here.

class Post(models.Model):
    """
    A post class that handles new posts to the website.
    Every post should have the following.
        1. A title
        2. Image if necessary
        3. Content
        4. Url to reference external links.
    """
    title = models.CharField(max_length=30, verbose_name='Post heading')
    img = models.ImageField(verbose_name='insert image')
    content = models.TextField(blank=False, verbose_name='Add post content')
    url = models.URLField(verbose_name='reference external links')

    def __str__(self) -> str:
        return self.title.lower()

    def __repr__(self) -> str:
        return self.title.capitalize()
