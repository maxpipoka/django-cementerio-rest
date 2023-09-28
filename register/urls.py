from django.urls import include, path
from rest_framework import routers
from register import views

router = routers.DefaultRouter()
# router.register('taxpayers', views.getTaxpayers, 'taxpayers')

urlpatterns = [
    path('', include(router.urls)),
    # path('taxpayers2/', views.TaxpayerApiView.as_view()),
    path('taxpayers/', views.getTaxpayers),
    path('taxpayers/add', views.addTaxpayer),
]
