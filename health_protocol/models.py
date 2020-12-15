from django.db import models

# Create your models here.
class Alternatives(models.Model):
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=150)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Name: {} | Text: {} | Upvotes: {} | Downvotes: {}".format(self.username, self.text, self.upvotes, self.downvotes)