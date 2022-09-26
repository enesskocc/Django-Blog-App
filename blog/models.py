from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()

    def postview_count(self):
        return self.postview_set.all().count()

    def comments(self):
        return self.comment_set.all()
    
    class Meta:
        ordering = ['-last_updated',]

    

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)



class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    

    

