from django.views.generic import View

from django.http import JsonResponse
from django.utils.crypto import get_random_string

from .models import Provider, Resource, Reservation

class ResourcesList(View):
	def get(self, request, category_id):
        resource_objects = Resource.objects.get(category = category_id)
		resources_json = JsonResponse({'resource_list': resource_objects})
		return resources_json

class ResourceInfo(View):
	def get(self, request, resource_id):
		resource_object = Resource.objects.get(pk = resource_id)[0]
		return JsonResponse({'resource': resource_object})

class TimeCheck(View):
	def get(request, resource_id, time_from, time_to):
		reservation_records = Reservation.objects.get(resource = resource_id)
		may_not_available = False
		for record in reservation_records:
			if record.time_begin < time_to and record.time_end > time_from:
				if record.status = True:
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
			snGenCount += 1
			if not Reservation.objects.get(sn = reserve_sn).exists():
				break
			if snGenCount > maxRetry:
				return JsonResponse({'success': 0, 'errmsg': 'reservation serial number generation failed.'})
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