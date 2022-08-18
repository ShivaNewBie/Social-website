from django.db.models.signals import pre_save 
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from blog.models import Blog


@receiver(pre_save,sender=Blog)
def add_slug_to_discussion(sender, instance, *args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = get_random_string(length=8)
        instance.slug = slug + '-' + random_string