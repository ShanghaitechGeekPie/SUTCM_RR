from django.views.generic import View

from django.http import JsonResponse
from django.utils.crypto import get_random_string

from .models import Resource, Reservation

import datetime

class ResourcesList(View):
	def get(self, request, category_id):
		resource_objects = Resource.objects.filter(pk = category_id)
		return JsonResponse({'resource_list': resource_objects})


class ResourceInfo(View):
	def get(self, request, resource_id):
		resource_object = Resource.objects.get(pk = resource_id)
		return JsonResponse({'resource': resource_object})


class TimeCheck(View):
	def get(request, resource_id, begin_at, duration):
		time_from = datetime.datetime.strptime(begin_at, '')
		time_to = datetime.datetime.strptime(begin_at, '') + datetime.datetime.timedelta(minutes = int(duration) * 30)
		# [REF]https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

		reservation_records = Reservation.objects.filter(
			resource = resource_id
		).filter(
			time_begin__lt = time_to
		).filter(
			time_end__gt = time_from
		)

		may_not_available = False

		for record in reservation_records:
			if record.status:
				return JsonResponse({'time_available': 0})
			else:
				may_not_available = True

		if may_not_available:
			return JsonResponse({'time_available': 2})
		return JsonResponse({'time_available': 1})


class Reserve(View):
	def post(request):
		# Reservation serial number generation
		snGenCount = 0
		maxRetry = 5
		while True:
			reserve_sn = get_random_string(length = 6)
			if not Reservation.objects.get(sn = reserve_sn).exists():
				break
			if snGenCount > maxRetry:
				return JsonResponse({'success': 0, 'errmsg': 'reservation serial number generation failed.'})
			snGenCount += 1
		# Write into database
		reservation = Reservation(
			sn = reserve_sn,
			applicant_phone = int(request.POST['applicant_phone']),
			applicant_name = request.POST['applicant_name'],
			applicant_department = int(request.POST['applicant_department']),
			applicant_sid = int(request.POST['applicant_sid']),
			resource = int(request.POST['resource_id']),
			purpose = request.POST['purpose'],
			time_begin = request.POST['time_begin'],
			time_end = request.POST['time_end']
		)
		try:
			reservation.save()
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': e})
		return JsonResponse({'success': 1, 'reserve_sn': reserve_sn})


class Result(View):
	def get(request, reserve_sn):
		destination_reservation = Reservation.objects.get(sn = reserve_sn)[0]
		return JsonResponse({'reservation': destination_reservation})