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
		if int(category_id) > 0:
			resource_objects = serializers.serialize('json', Room.objects.filter(category = int(category_id)))
		else:
			resource_objects = serializers.serialize('json', Room.objects.all())
		resources_response = json_head + resource_objects + json_tail
		return HttpResponse(resources_response)

class ResourceInfo(View):
	def get(self, request, room_id):
		try:
			room_object = Room.objects.get(pk = resource_id)
			room_content = {
				'success': 1,
				'category': room_object.category,
				'name': room_object.name,
				'location': room_object.location,
				'capacity': room_object.capacity,
				'description': room_object.description,
				'provider_name': room_object.provider_name,
				'open_hours': room_object.open_hours
			}
			return JsonResponse(room_content)
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': str(e)})


class TimeCheck(View):
	def get(self, request, room_id, yyyy, mm, dd, hr, minu, sec, duration):
		try:
			time_from = datetime.datetime(year = int(yyyy), month = int(mm), day = int(dd), hour = int(hr), minute = int(minu), second = int(sec))
			time_to = time_from + datetime.timedelta(minutes = int(duration) * 30)

			reservation_records = Reservation.objects.filter(
				room = room_id
			).filter(
				time_begin__lt = time_to
			).filter(
				time_end__gt = time_from
			)

			may_not_available = False

			for record in reservation_records:
				if record.status:
					return JsonResponse({'success': 1, 'time_available': 0})
				else:
					may_not_available = True

			if may_not_available:
				return JsonResponse({'success': 1, 'time_available': 2})
			return JsonResponse({'success': 1, 'time_available': 1})
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': str(e)})


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
			room = int(request.POST['room_id']),
			purpose = request.POST['purpose'],
			time_begin = request.POST['time_begin'],
			time_end = request.POST['time_end'],
			img = request.POST['img_src']
		)
		try:
			reservation.save()
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': str(e)})
		return JsonResponse({'success': 1, 'reserve_sn': reserve_sn})


class Result(View):
	def get(self, request, reserve_sn):
		try:
			reservation_object = Reservation.objects.get(sn = reserve_sn)
			reservation_content = {
				'success': 1,
				'applicant': {
					'name': reservation_object.applicant_phone,
					'department': reservation_object.applicant_department.name,
					'sid': reservation_object.applicant_sid
				},
				'room': {
					'name': reservation_object.room.name,
					'location': reservation_object.room.location,
				},
				'category': reservation_object.category.name,
				'time_from': reservation_object.time_begin,
				'time_to': reservation_object.time_end,
				'status': reservation_object.status
			}
			return JsonResponse(reservation_content)
		except Exception as e:
			return JsonResponse({'success': 0, 'errmsg': str(e)})