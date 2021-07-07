from django.db import models
from datetime import datetime


# Create your models here.

class create_user(models.Model):
    user_id=models.AutoField(primary_key=True)
    destination=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)
    team_member=models.CharField(max_length=100)
    needed_member=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    address=models.CharField(max_length=300)
    fblink=models.CharField(max_length=300,default="")
    twitterlink=models.CharField(max_length=300,default="")
    national_id_image=models.ImageField(upload_to="tourshare/images",default="")
    create_user_image=models.ImageField(upload_to="tourshare/images",default="")
class create_team(models.Model):
    team_id=models.AutoField(primary_key=True)
    group_name=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    team_member=models.CharField(max_length=100)
    needed_member=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
      return self.group_name
class join_user(models.Model):
     team_id=models.AutoField(primary_key=True)
     group_name=models.CharField(max_length=100)
     team_member=models.CharField(max_length=100)
     email=models.EmailField(max_length=100,default="0")
     phone_number=models.CharField(max_length=100)
     address=models.CharField(max_length=300)
     fblink=models.CharField(max_length=300,default="")
     twitterlink=models.CharField(max_length=300,default="")
     national_id_image=models.ImageField(upload_to="tourshare/images",default="")
     join_user_image=models.ImageField(upload_to="tourshare/images",default="")

  
    
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
