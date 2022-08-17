from django.db import models


from core.models import TimeStamp


class Blog(TimeStamp):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
