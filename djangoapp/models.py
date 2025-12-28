from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    #django kendi ekler am aben ekledim yine de 
    id = models.BigAutoField(primary_key=True)
    #user tarafının gördüğü urlde id görünmesin diye public id 
    

    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)