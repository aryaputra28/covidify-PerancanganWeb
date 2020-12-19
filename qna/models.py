from django.db import models
from django.utils import timezone

# Create your models here.
class pertanyaan(models.Model):
    penanya = models.CharField(max_length=400)
    pertanyaan = models.TextField(max_length=800)
    location = models.TextField(max_length=400,default="Depok")
    time = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="gilangcaturyudistira@gmail.com")
    
    def __str__(self):
        return "{} | {} ".format(self.penanya,self.pertanyaan)

class komentar(models.Model):
    pengomentar = models.CharField(max_length=400)
    komen = models.TextField(max_length =800)
    tanya = models.ForeignKey(pertanyaan, on_delete = models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    location = models.TextField(max_length=400, default="Depok")
    email = models.EmailField(default="gilang.catur@ui.ac.id")

    def __str__(self):
        return "{} | {} | {} ".format(self.tanya.pertanyaan,self.pengomentar,self.komen)