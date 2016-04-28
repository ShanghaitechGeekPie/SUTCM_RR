from django.db import models

class Applicant(models.Model):
	cellphone_num = models.BigIntegerField()
	#? Foreign student name
	name = models.CharField(max_length=30)
	department = models.PositiveSmallIntegerField()

class Provider(models.Model):
	name = models.CharField()
	description = models.TextField()

class Resource(models.Model):
	category = models.PositiveSmallIntegerField()
	name = models.CharField()
	location = models.CharField()
	capacity = models.PositiveSmallIntegerField()
	provider = models.ForeignKey('Provider')

class Reservation(models.Model):
	applicant = models.ForeignKey('Applicant')
	resource = models.ForeignKey('Resource')
	status = models.NullBooleanField()

