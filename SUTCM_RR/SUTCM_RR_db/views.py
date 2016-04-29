from django.views.generic import View

from django.http import JsonResponse
from django.utils.crypto import get_random_string

from .models import Provider, Resource, Reservation

class ResourceList(View):
    def get(self, request, category_id):
        resource_objects = Resource.objects.get(category = category_id)
		resources_json = JsonResponse({'resource_list': resource_objects})
		return resources_json

class ResourceInfo(request, id):
	def get(self, request, *args, **kwargs):
		resource
		resource_json = JsonResponse()
		return resource_json

def time_check(request, resource_id, time):
	reservation_records = Reservation.objects.get(resource = resource_id)
	may_not_available = False
	for record in reservation_records:
		if record.time_begin < time[1] & record.time_end > time[0]:
			if record.status = True:
				return JsonResponse({'time_available': 0})
			else:
				may_not_available = True
	if may_not_available:
		return JsonResponse({'time_available': 2})
	return JsonResponse({'time_available': 1})


def reserve(request, type):
	# Get Reservation Serial Number
	snGenCount = 0
	maxRetry = 5
	while True:
		reserve_sn = get_random_string(length = 6)
		loopContinueFlag += 1
		if not Reservation.objects.get(sn = reserve_sn).exists():
			break
		if snGenCount > maxRetry:
			return JsonResponse({'errmsg': 'reservation serial number generation failed.'})
	# Write into database

	return JsonResponse({'success': 1, 'reserve_sn': reserve_sn})


def result(request, reserve_sn):
	destination_reservation = Reservation.objects.get(sn = reserve_sn)
	result_json = JsonResponse({'reservation': destination_reservation})
	return result_json