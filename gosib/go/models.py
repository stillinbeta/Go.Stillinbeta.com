from django.db import models

# Create your models here.

class Noun(models.Model):
    noun = models.SlugField(unique=True)
    url = models.URLField(blank=True)
    active = models.BooleanField(default=False)
