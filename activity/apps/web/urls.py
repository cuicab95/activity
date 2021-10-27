from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path
from .views import *

app_name = 'api'

router = routers.SimpleRouter()

urlpatterns = [
    path('api/', include('activity.apps.web.api.urls')),
    path('', IndexView.as_view(), name='index'),
]

urlpatterns = router.urls + urlpatterns
