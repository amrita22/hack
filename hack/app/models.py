# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.




class HackData(models.Model):
	problem_statement = models.TextField(null=True)
	identifier = models.CharField(null=True, max_length=300)
	attribute1 = models.CharField(null=True, max_length=300)
	attribute2 = models.CharField(null=True, max_length=300)
	attribute3 = models.CharField(null=True, max_length=300)
	attribute4 = models.CharField(null=True, max_length=300)
	attribute5 = models.CharField(null=True, max_length=300)
	target = models.CharField(null=True, max_length=300)
	genre = models.CharField(null=True, max_length=300)

	def __unicode__(self):
		return unicode(self.name)


     