# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.CharField(max_length=50)
    birth_date = models.DateField()
    picture = models.URLField(blank=False)
    employer = models.CharField(max_length=100)
    occupation = models.CharField(max_length=30)
    net_worth = models.DecimalField(decimal_places=2)

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})
