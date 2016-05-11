"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from SUTCM_RR_db import views as db_views

admin.site.site_title = '上海中医药大学学生事务中心预约平台'
admin.site.site_header = '上海中医药大学资源预约平台管理'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # return: all rooms
    url(r'^rooms/$', db_views.ResourcesList.as_view(), {'category_id': -1}, name = 'all_rooms'),
    # return: all rooms that can handle certain reservation type
    url(r'^rooms/(?P<category_id>\d{1})/$', db_views.ResourcesList.as_view(), name = 'rooms'),
    # return: room detail
    url(r'^room/(?P<room_id>\d+)/$', db_views.ResourceInfo.as_view(), name = 'room'),
    # return: 0 - not available, 1 - available, 2 - have pending requests overlapping in time
    # time/room_id/yyyy/mm/dd/duration
    # duration: an integer x, meaning that the reservation will last 30x minutes
    url(r'^time/(?P<room_id>\d+)/(?P<yyyy>\d{4})/(?P<mm>\d{2})/(?P<dd>\d{2})/(?P<duration>\d{1})/$', db_views.TimeCheck.as_view(), name = 'time_check'),
    url(r'^reserve/$', db_views.Reserve.as_view(), name = 'reserve'),
    url(r'^result/(?P<reserve_sn>\d|\w{6})/$', db_views.Result.as_view(), name = 'result')
]