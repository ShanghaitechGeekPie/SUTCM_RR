from django.db import models

class Provider(models.Model):
	name = models.CharField()
	description = models.TextField(blank = True)

class Resource(models.Model):
	CATEGORIES = (
		(0, '活动室'),
		('咨询', (
			(1, '创业'), (2, '就业'), (3, '心理')
		))
	)

	category = models.PositiveSmallIntegerField(choices = CATEGORIES, verbose_name = '种类')
	name = models.CharField(max_length = 20, verbose_name = '资源名称')
	location = models.CharField(max_length = 20, verbose_name = '位置')
	capacity = models.PositiveSmallIntegerField(verbose_name = '最大容纳人数')
	description = models.TextField(blank = True, verbose_name = '简介')
	provider = models.ForeignKey(Provider, verbose_name = '负责人')
	#? Photo and other static resources

class Reservation(models.Model):
# parameters and data
	DEPARTMENT_CHOICES = (
		(0,'A学院')
	)

# model field definitions
	applicant_phone = models.BigIntegerField(unique = True, verbose_name = '手机号')
	#? Foreign student name
	applicant_name = models.CharField(max_length = 30, verbose_name = '姓名')
	applicant_department = models.PositiveSmallIntegerField(verbose_name = '学院')

	resource = models.ForeignKey('Resource')
	# null for pending, True for accepted, False for rejected.
	status = models.NullBooleanField()
	purpose = models.CharField(max_length = 50, blank = True, verbose_name = '使用目的')
	''' switch(resource.category)
		case room: duration should be 30, 60, 90, ..., 240 min.s and starts from XX:00 or XX:30
		case consultation: no specific constraint
	availability_check: begin2 < end && end2 > begin
	'''
	time_begin = models.DateTimeField(verbose_name = '开始时间')
	time_end = models.DateTimeField(verbose_name = '结束时间')

	checkcode = models.CharField(max_length = 255, verbose_name = '查询代码')