from django.db import models, connection


# Other functions
def get_post(default='all'):
    """
    A function that returns the provided post category.
    """
    post_choice = [
        (1, 'about us summary'),
        (2, 'mission'),
        (3, 'vision'),
        (4, 'event'),
        (5, 'about us full'),
        (6, 'offer'),
        (7, 'creed'),
        (8, 'core values'),
        (9, 'school anthem')
    ]
    if default == 'all':
        return post_choice
    else:
        # values = list(post_dict.values())
        # if default in values:
        result = ''.join([str(value[0]) for value in post_choice if default in value[1]])
        return int(result)

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
    post_choice = get_post()
    post_category = models.IntegerField(verbose_name='Post category', choices=post_choice, default=4)
    title = models.CharField(max_length=100, verbose_name='Post heading')
    img = models.ImageField(verbose_name='Insert image', upload_to='images/', blank=True)
    content = models.TextField(blank=False, verbose_name='Add post content')
    url = models.URLField(verbose_name='Reference external links', blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title.lower()

    def __repr__(self) -> str:
        return self.title.capitalize()
    
    class Meta:
        verbose_name = 'School Post'
        verbose_name_plural = 'School Posts'

class UpdateImage(models.Model):
    """
    A web service to manage the images on the web homepage.
    """
    # img_list = models.AutoField(verbose_name='Image list')
    img_choices = [
        (1, 'gallery'), (2, 'homepage'), (3, 'all'), (4, 'labs'), (5, 'reception'),
        (6, 'nursery/primary'), (7, 'secondary'), (8, 'classes'), (9, 'workshops'),
        (10, 'sports')
        ]
    img_tag = models.CharField(verbose_name='Image description', max_length=200)
    img = models.ImageField(verbose_name='Select image', upload_to='images/')
    img_use = models.IntegerField(verbose_name='Page image assignment', choices=img_choices, default=3)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def publish(self, img_id):
        pass

    def select_image(self):
        images = UpdateImage.objects.all()
        print(images)
    
    def __str__(self):
        return str(self.img_tag)

    def __repr__(self) -> str:
        return str(self.img_tag)

    class Meta:
        verbose_name = 'School Image'
        verbose_name_plural = 'School Images'