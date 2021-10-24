from rest_framework import routers
from django.conf.urls import url, include

app_name = 'api'

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^api/', include('activity.apps.web.api.urls'))
]

urlpatterns = router.urls + urlpatterns
