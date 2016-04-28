from django.db import models

class Applicant(models.Model):
# parameters and data
	DEPARTMENT_CHOICES = (
		(0,'A学院'),
	)

# model field definitions
	cellphone_num = models.BigIntegerField(unique = True, verbose_name = '手机号')
	#? Foreign student name
	name = models.CharField(max_length = 30, verbose_name = '姓名')
	department = models.PositiveSmallIntegerField(verbose_name = '学院')

class Provider(models.Model):
	name = models.CharField()
	description = models.TextField(blank = True)

class Resource(models.Model):
	CATEGORIES = (
		(1, '活动室'),
		('咨询', (
			(2, '创业'), (3, '就业'), (4, '心理')
		))
	)

	category = models.PositiveSmallIntegerField(choices = CATEGORIES)
	name = models.CharField()
	location = models.CharField()
	capacity = models.PositiveSmallIntegerField()
	description = models.TextField(blank = True)
	provider = models.ForeignKey(Provider)
	#? Photo and other static resources

class Reservation(models.Model):
	applicant = models.ForeignKey('Applicant')
	resource = models.ForeignKey('Resource')
	status = models.NullBooleanField()
	purpose = models.CharField(blank = True)
	''' switch(resource.category)
		case room: duration should be 30, 60, 90, ..., 240 min.s and starts from XX:00 or XX:30
		case consultation: no specific constraint
	'''
	time_begin = models.DateTimeField()
	time_end = models.DateTimeField()