from django.views.generic import View

from django.http import HttpResponse, JsonResponse
from django.utils.crypto import get_random_string
from django.core import serializers

from .models import Category, Department, Room, Reservation

import datetime

class ResourcesList(View):
	def get(self, request, category_id):
		json_head = '{"success": 1, "resources": '
		json_tail = '}'
		resource_objects = serializers.serialize('json', Resource.objects.filter(category = int(category_id)))
		resources_response = json_head + resource_objects + json_tail
		return HttpResponse(resources_response)

class ResourceInfo(View):
	def get(self, request, resource_id):
		try:
			resource_object = Resource.objects.get(pk = resource_id)
			resource_content = {
				'success': 1,
				'category': resource_object.category,
				'name': resource_object.name,
				'location': resource_object.location,
				'capacity': resource_object.capacity,
				'description': resource_object.description,
				'provider_name': resource_object.provider_name,
				'open_hours': resource_object.open_hours
			}
			return JsonResponse(resource_content)
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': e})


class TimeCheck(View):
	def get(self, request, resource_id, yyyy, mm, dd, duration):
		try:
			time_from = datetime.datetime(year = int(yyyy), month = int(mm), day = int(dd))
			time_to = time_from + datetime.timedelta(minutes = int(duration) * 30)
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
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': e})


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
		# TODO validation before creating the model instance
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