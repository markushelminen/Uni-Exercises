from __future__ import unicode_literals
from datetime import datetime   
from django.db import models
from django.forms.widgets import NumberInput

# Create your models here.


class Search(models.Model):
    palvelu_choices = (
    ('restaurant', 'Restaurants'),
    ('bar', 'Bars'),
    ('store', 'Stores'),
    ('barber', 'Barbers')
    )
    
    user = models.CharField(max_length=30)
    service =  models.CharField(max_length=30, choices=palvelu_choices)
    radius = models.IntegerField(default=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    

    