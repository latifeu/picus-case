from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    #django adds id block but i add already 
    id = models.BigAutoField(primary_key=True)

    

    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)