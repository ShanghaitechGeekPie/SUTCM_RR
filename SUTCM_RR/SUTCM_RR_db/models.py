from django.db import models

class Provider(models.Model): # 资源负责人（社团指导老师，电教员……）
	name = models.CharField(max_length = 20)
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

	time_open_begin = models.DateTimeField(verbose_name = '开放时间')
	time_open_end = models.DateTimeField(verbose_name = '结束时间')
	#? Photo and other static resources


class Reservation(models.Model):
# parameters and data
	DEPARTMENT_CHOICES = (
		(0,'A学院')
	)

# model field definitions
	applicant_phone = models.BigIntegerField(unique = True, verbose_name = '申请人手机号')
	#? Foreign student name
	applicant_name = models.CharField(max_length = 30, verbose_name = '申请人姓名')
	applicant_department = models.PositiveSmallIntegerField(verbose_name = '申请人学院')
	applicant_sid = models.PositiveSmallIntegerField(verbose_name = '申请人学号')

	resource = models.ForeignKey('Resource')
	# null for pending, True for accepted, False for rejected.
	status = models.NullBooleanField(default = None)
	purpose = models.CharField(max_length = 50, blank = True, verbose_name = '申请用途')
	
	time_begin = models.DateTimeField(verbose_name = '开始时间')
	time_end = models.DateTimeField(verbose_name = '结束时间')

	sn = models.CharField(unique = True, max_length = 5, verbose_name = '查询代码')