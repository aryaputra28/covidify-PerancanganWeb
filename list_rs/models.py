from django.db import models

class Rumah_Sakit(models.Model):
    provinsi = models.CharField(max_length=100)
    nama_rs = models.CharField(max_length=100)
    alamat = models.CharField(max_length=1000)
    telepon = models.IntegerField()
    website = models.CharField(max_length=1000)
