from django.db import models

# Create your models here.
class Scholarships(models.Model):
    title = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    description = models.TextField()
    url = models.CharField(max_length=200)
    closing_date = models.DateTimeField()