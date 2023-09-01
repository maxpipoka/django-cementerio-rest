from django.urls import include, path
from rest_framework import routers
from register import views

router = routers.DefaultRouter()
router.register(r'taxpayers', views.TaxpayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
