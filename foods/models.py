from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PRIORITIES = ((1, 'Bad'), (2, 'Good'))

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    ingradients = models.TextField(max_length=400)
    # image_url = models.ImageField()
    def __unicode__(self):
        return self.food_name

class Rating(models.Model):
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    stars = models.IntegerField(default=0, choices=PRIORITIES)
    description = models.TextField(max_length=400)

