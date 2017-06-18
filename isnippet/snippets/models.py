from django.db import models

# Create your models here.

class Snippet(models.Model):
	title = models.CharField(max_length= 75),
	language = models.Charfield(max_legth = 30),
	description = models.Charfield(max_length = 100),
	content = models.Charfield(max_length = 400),

	def __str__(self):              
        return self.title