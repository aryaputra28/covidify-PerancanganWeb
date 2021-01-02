from django.contrib import admin
from .models import Alternative, Upvote

# Register your models here.
admin.site.register(Alternative)
admin.site.register(Upvote)