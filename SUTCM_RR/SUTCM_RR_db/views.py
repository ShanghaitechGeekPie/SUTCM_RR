from django.http import JsonResponse

from .models import Provider, Resource, Reservation

def resource_list(request):
	resource_objects = Resource.objects
	resources_json = JsonResponse({'resource_list': resource_objects})
	return resources_json

def resource(request, id):
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
	if succeeded:
		reservation_response = JsonResponse({'success': 1, 'reserve_sn': reserve_sn})
	return reservation_response


def result(request, reserve_sn):
	destination_reservation = Reservation.objects.get(sn = reserve_sn)
	result_json = JsonResponse({'reservation': destination_reservation})
	return result_json