from django.db import models

# Create your models here.

class Rapid(models.Model):
    nama_tempat = models.CharField(max_length=100)
    tanggal_pelaksanaan_mulai = models.DateField(auto_now_add=False, auto_now=False, null=True)
    tanggal_pelaksanaan_akhir = models.DateField(auto_now_add=False, auto_now=False, null=True)
    biaya = models.DecimalField(max_digits=6, decimal_places=3)
    alamat = models.TextField()