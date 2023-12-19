from django.urls import include, path
from rest_framework import routers
from register import views

router = routers.DefaultRouter()
router.register(r'taxpayer', views.TaxpayerViewset, 'taxpayer')
router.register(r'deceased', views.DeceasedViewset, 'deceased')
router.register(r'state', views.StateViewset, 'state')
router.register(r'county', views.CountyViewset, 'county')
router.register(r'city', views.CityViewset, 'city')
router.register(r'registrationoffice', views.RegistrationOfficeViewset, 'registrationoffice')
router.register(r'burialpermit', views.BurialPermitViewset, 'burialpermit')
router.register(r'sector', views.SectorViewset, 'sector')
router.register(r'periodicity', views.PeriodicityViewset, 'periodicity')
router.register(r'parcel', views.ParcelViewset, 'parcel')
router.register(r'grave', views.GraveViewset, 'grave')
router.register(r'tax', views.TaxViewset, 'tax')
router.register(r'payment', views.PaymentViewset, 'payment')


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

