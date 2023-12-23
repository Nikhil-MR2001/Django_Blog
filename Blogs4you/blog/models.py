from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/')
    created = models.DateTimeField(auto_now_add=True)

    # to show the image as image(not path) in admin panel
    def image_tag(self):
        return format_html('<img src="/media/{}"  style="border-radius: 50%; width:40px; height:40;" />'.format(self.image))

    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
