from django.db import models

# Create a blog model

class blog(models.Model):
	title=models.CharField(max_length=255)
	pub_date=models.DateTimeField()
	body=models.TextField()
	image=models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pret(self):
		return self.pub_date.strftime('%b %e %Y')

