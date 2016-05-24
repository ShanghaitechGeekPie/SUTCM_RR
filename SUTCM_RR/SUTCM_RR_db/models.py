from django.db import models

# class Provider(models.Model): # 资源负责人（社团指导老师，电教员……）
# 	name = models.CharField(max_length = 20)
# 	description = models.TextField(blank = True)

# CAT_NAMES = ['活动室', '创业咨询', '就业咨询', '心理咨询']

class Category(models.Model):
	name = models.CharField(max_length = 10, verbose_name = '预约用途')

	class Meta:
		verbose_name = "用途种类"
		verbose_name_plural = "用途种类"

	def __str__(self):
		return self.name + '预约'


class Department(models.Model):
	name = models.CharField(max_length = 50, verbose_name = '院系/专业名称')

	class Meta:
		verbose_name = "院系/专业"
		verbose_name_plural = "院系/专业"

	def __str__(self):
		return self.name


class Room(models.Model):
	category = models.ManyToManyField(Category, verbose_name = '可预约用途')
	name = models.CharField(max_length = 20, verbose_name = '房间名称')
	location = models.CharField(max_length = 20, verbose_name = '位置')
	capacity = models.PositiveSmallIntegerField(verbose_name = '最大承载人数')
	#description = models.TextField(blank = True, verbose_name = '简介')
	provider_name = models.CharField(max_length = 20, verbose_name = '负责人')

	open_hours = models.CharField(max_length = 50, verbose_name = '开放时间')
	img = models.CharField(max_length = 50, verbose_name = '照片路径')

	class Meta:
		verbose_name = '房间'
		verbose_name_plural = '房间'

	def __str__(self):
		return '{} @{}'.format(self.name, self.location)


class Reservation(models.Model):
	applicant_phone = models.BigIntegerField(unique = True, verbose_name = '申请人手机号')
	#? Foreign student name
	applicant_name = models.CharField(max_length = 30, verbose_name = '申请人姓名')
	applicant_department = models.ForeignKey(Department, verbose_name = '申请人学院')
	applicant_sid = models.PositiveSmallIntegerField(verbose_name = '申请人学号')

	room = models.ForeignKey(Room, verbose_name = '申请房间')
	category = models.ForeignKey(Category, verbose_name = '预约种类')
	# null for pending, True for accepted, False for rejected.
	status = models.NullBooleanField(default = None, verbose_name = '申请通过状态')
	people = models.PositiveSmallIntegerField(verbose_name = '使用人数')
	purpose = models.TextField(max_length = 50, blank = True, verbose_name = '具体申请用途')

	time_begin = models.DateTimeField(verbose_name = '开始时间')
	time_end = models.DateTimeField(verbose_name = '结束时间')

	sn = models.CharField(unique = True, max_length = 6, verbose_name = '查询代码')

	class Meta:
		verbose_name = '预约'
		verbose_name_plural = '预约'
