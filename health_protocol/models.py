from django.db import models
from main.models import Pengguna

# Create your models here.
class Alternative(models.Model):
    author = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='author')
    text = models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(Pengguna, default=None, blank=True, related_name='liked')

    def __str__(self):
        return "Author: {} | Text: {} | Upvotes: {}".format(self.author.namalengkap, self.text, self.num_upvotes)

    @property
    def num_upvotes(self):
        return self.liked.all().count()

UPVOTE_CHOICES = (
    ('Boleh tuh!', 'Boleh tuh!'),
    ('Skip deh...', 'Skip deh...'),
)

class Upvote(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    alternatives = models.ForeignKey(Alternative, on_delete=models.CASCADE)
    value = models.CharField(choices=UPVOTE_CHOICES, default='Boleh tuh!', max_length=30)

    def __str__(self):
        return "ID: {} | Likers: {}".format(self.alternatives.id, self.alternatives.liked.all())
