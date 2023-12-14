from django.urls import include, path
from rest_framework import routers
from register import views

router = routers.DefaultRouter()
router.register(r'taxpayers', views.TaxpayerViewset, 'taxpayers')

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('taxpayers2/', views.TaxpayerApiView.as_view()),
#     path('taxpayers/', views.getTaxpayers),
#     path('taxpayers/add', views.addTaxpayer),
#     path('taxpayers/<int:id>', views.getOneTaxpayer)
# ]

urlpatterns = [
    path('', include(router.urls))
]

