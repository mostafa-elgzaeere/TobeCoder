from django.db import models

# Create your models here.
from django.db.models import *
from django.contrib.auth.models import User
# Create your models here.



class Track(Model):
    name=CharField(max_length=100)
    image=ImageField(upload_to="static/img",height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name




class Curse(Model):
    name=CharField(max_length=100)
    image=ImageField(upload_to="static/img",height_field=None, width_field=None, max_length=None)
    track=ForeignKey(Track,on_delete=CASCADE,related_name="curses")

    def __str__(self):
        return self.name



class Video(Model):
    title=CharField(max_length=200)
    description=TextField(max_length=300)
    url=URLField(max_length=200)
    will_learn=CharField(max_length=300)
    requierments=CharField(max_length=300)
    curse=ForeignKey(Curse,on_delete=CASCADE,related_name="videos")


    
    def __str__(self):
        return self.title


 