from django.db import models
from django import forms

# Create your models here.



class Post(models.Model): #camera_category


    nome      = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=15)
    serie       = models.CharField(max_length=16)
    
#python 3
    def __str__(self):
        return self.nome
    
#python 2
    def __unicode__(self):
        return self.nome
