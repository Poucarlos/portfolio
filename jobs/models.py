from django.db import models

# models.Model helps create the object to save inside the database
class Job(models.Model):
	image=models.ImageField(upload_to='images/')#the '' space is where does the immage will be stored
	summary = models.CharField(max_length=200)
