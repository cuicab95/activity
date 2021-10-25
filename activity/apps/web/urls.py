from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path

app_name = 'api'

router = routers.SimpleRouter()

urlpatterns = [
    path('api/', include('activity.apps.web.api.urls'))
]

urlpatterns = router.urls + urlpatterns
