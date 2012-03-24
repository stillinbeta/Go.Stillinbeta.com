from random import randint

from django.db import models


# Create your models here.

class NounManager(models.Manager):
    def shorten(self, url):
        elements = self.filter(active=False).count()
        if not elements:
            raise Noun.DoesNotExist()
        random_idx = randint(0, elements - 1)
        noun = self.filter(active=False)[random_idx]
        noun.url = url
        noun.active = True
        noun.save()
        
        return noun

class Noun(models.Model):
    noun = models.SlugField(unique=True)
    url = models.URLField(blank=True)
    active = models.BooleanField(default=False)

    def follow(self):
        self.url = ""
        self.active = False
        self.save()

    objects = NounManager()
