from rest_framework import routers
from django.conf.urls import url
from .views import *
app_name = 'api'

router = routers.SimpleRouter()
router.register(r'activity', AddActivityViewSet)

urlpatterns = [
    #url(r'^add-activity/', AddActivityView.as_view()),
]

urlpatterns = router.urls + urlpatterns
