

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from taggit.managers import  TaggableManager

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES=(('draft','DRAFT'),('published','PUBLISHED'))
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique_for_date='publish')
    body=models.TextField()
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=False)
    publish=models.DateTimeField(default=timezone.now())
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
    tag=TaggableManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])


#create comments model
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=False)
    name=models.CharField(max_length=40)
    email=models.EmailField()
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return "created by {} on {}".format(self.name,self.post)
