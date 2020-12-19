from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    nama = models.CharField(max_length=100)
    feedbackUser = models.TextField(max_length=1000)
    
class Pengguna(models.Model):
    namalengkap = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    institusi = models.CharField(max_length=100)
    akun = models.ForeignKey(User,on_delete=models.CASCADE)