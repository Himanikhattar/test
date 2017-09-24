# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserDB(models.Model):

	auto_increment_id = models.AutoField(primary_key=True)

	name = models.CharField(max_length=100, null=True, blank=True)	
	phone = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	GENDER_CHOICES = (
        ('M','Male'),
        ('F','female')
        )
	gender = models.CharField(choices=GENDER_CHOICES,max_length=10 ,null=True, blank=True)
	about_me = models.TextField(null=True)
