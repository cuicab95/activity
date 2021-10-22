from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
#router.register(r'application', ApplicationViewSet)

urlpatterns = [
    #path('add-device/', CreateUserDeviceView.as_view()), example
]

urlpatterns = router.urls + urlpatterns
