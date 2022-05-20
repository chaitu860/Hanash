from django.db import models
from django.contrib.auth.models import User

class HanashUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=12)
    bio=models.TextField(max_length=200,default="live a happy life")
    profile_pic=models.ImageField(upload_to='profile_pic/')


class Room(models.Model):
    room_name=models.CharField(max_length=200,primary_key=True)
    tag=models.CharField(max_length=200)


class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
    content=models.TextField(max_length=200)
    room=models.ForeignKey(Room, on_delete=models.CASCADE,related_name="room")
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('date_created',)
       
class Posts(models.Model):
    
    id=models.IntegerField(primary_key=True,default=1)
    image=models.ImageField(upload_to='posts/')
    date_created=models.DateTimeField(auto_now_add=True)
    caption=models.CharField(max_length=200)
    tag=models.CharField(max_length=200)
    creator=models.ForeignKey(HanashUser, on_delete=models.CASCADE)
    likes=models.ManyToManyField(HanashUser,related_name="likes",default="False")
    likes_count=models.IntegerField(default=1)

class Comments(models.Model):
    comment_post=models.ForeignKey(Posts, on_delete=models.CASCADE,related_name="post_img")
    comment_author=models.ForeignKey(HanashUser, on_delete=models.CASCADE,related_name="author")
    date_created=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(max_length=200)


# Create your models here.
