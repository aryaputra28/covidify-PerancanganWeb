from django.db import models
from django.contrib.auth.models import User
from main.models import Pengguna
from django.utils import timezone

# Create your models here.
class Alternatives(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} | Text: {} | Upvotes: {} | Downvotes: {}".format(self.pengguna, self.text, self.upvotes, self.downvotes)

class Preference(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE, null=True)
    alternatives = models.ForeignKey(Alternatives, on_delete=models.CASCADE, null=True)

    # value: 1 = like, 2 = dislike
    value = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pengguna) + ' | ' + str(self.alternatives) + ' | Values: ' + str(self.value)

    class Meta:
        unique_together = ("pengguna", "alternatives", "value")

