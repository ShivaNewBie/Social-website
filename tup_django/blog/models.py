from django.db import models

from django.conf import settings

from core.models import TimeStamp




class Blog(TimeStamp):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def name(self):
        return str(self.author.first_name) + ' '  + str(self.author.last_name)
        