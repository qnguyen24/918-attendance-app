import datetime
from django.db import models
from django.utils import timezone


class Cadet(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=50)
	
	def __str__(self):
		#"to-string" method for cadets, in a 'lastname, firstname' format
		return self.lastName + ', ' + self.firstName

class Day(models.Model):
	date = models.DateTimeField()
	cadetsPresent = models.ManyToManyField(Cadet)
	
	def __str__(self):
		#"to-string" method for a day
		return str(self.date)

class Flight(models.Model):
	name = models.CharField(max_length=25)
	nickname = models.CharField(max_length=100)
	useNickname = models.BooleanField(default=False)
	cadets = models.ManyToManyField(Cadet, related_name='+')
	
	def __str__(self):
		if self.useNickname:
			return self.nickname + ' (' + self.name + ' flight)'
		else:
			return self.name + ' flight'

