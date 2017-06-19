from django.db import models

# Create your models here.

class Snippet(models.Model):
	title = models.CharField(max_length= 75),
	language = models.CharField(max_length = 30),
	description = models.CharField(max_length = 100),
	content = models.CharField(max_length = 400),

def __str__(self):              
    return self.title