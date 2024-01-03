from django.urls import include, path
from rest_framework import routers
from register.views import (burialPermitViews,
                            cityViews, countyViews, deceasedViews,
                            graveViews,
                            parcelViews,
                            paymentViews,
                            periodicityViews,
                            registrationOfficeViews,
                            sectorViews, stateViews,
                            taxViews, taxpayerViews)
from register import views

router = routers.DefaultRouter()
router.register(r'taxpayer', taxpayerViews.TaxpayerViewset, 'taxpayer')
router.register(r'deceased', deceasedViews.DeceasedViewset, 'deceased')
router.register(r'state', stateViews.StateViewset, 'state')
router.register(r'county', countyViews.CountyViewset, 'county')
router.register(r'city', cityViews.CityViewset, 'city')
router.register(r'registrationoffice', registrationOfficeViews.RegistrationOfficeViewset, 'registrationoffice')
router.register(r'burialpermit', burialPermitViews.BurialPermitViewset, 'burialpermit')
router.register(r'sector', sectorViews.SectorViewset, 'sector')
router.register(r'periodicity', periodicityViews.PeriodicityViewset, 'periodicity')
router.register(r'parcel', parcelViews.ParcelViewset, 'parcel')
router.register(r'grave', graveViews.GraveViewset, 'grave')
router.register(r'tax', taxViews.TaxViewset, 'tax')
router.register(r'payment', paymentViews.PaymentViewset, 'payment')


urlpatterns = [
    path('', include(router.urls))
]

