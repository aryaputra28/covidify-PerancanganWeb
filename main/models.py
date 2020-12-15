from django.db import models

# Create your models here.

class Feedback(models.Model):
    nama = models.CharField(max_length=100)
    feedbackUser = models.TextField(max_length=1000)
    