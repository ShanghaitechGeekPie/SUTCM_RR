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
from SUTCM_RR_db.views import ResourcesList, ResourceInfo, TimeCheck, Reserve, Result

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^resources/(?P<category_id>\d{1})/$', ResourcesList.as_view(), name = 'resources'),
    url(r'^resource/(?P<resource_id>\d+)/$', ResourceInfo.as_view(), name = 'resource'),
    url(r'^time/(?P<resource_id>\d+)/(?P<from>\d+)/(?P<to>\d+)/$', TimeCheck.as_view(), name = 'time_check'),
    url(r'^reserve/$', Reserve.as_view(), name = 'reserve'),
    url(r'^result/(?P<reserve_sn>\d|\w{6})/$', Result.as_view(), name = 'result')
]