from django.urls import include, path
from rest_framework import routers
from register.views import (taxpayer,
                            deceased,
                            state, county,
                            burialPermit,
                            city,
                            grave,
                            parcel,
                            payment,
                            periodicity,
                            registrationOffice,
                            sector,
                            tax)
from register import views

router = routers.DefaultRouter()
router.register(r'taxpayer', taxpayer.TaxpayerViewset, 'taxpayer')
router.register(r'deceased', deceased.DeceasedViewset, 'deceased')
router.register(r'state', state.StateViewset, 'state')
router.register(r'county', county.CountyViewset, 'county')
router.register(r'city', city.CityViewset, 'city')
router.register(r'registrationoffice', registrationOffice.RegistrationOfficeViewset, 'registrationoffice')
router.register(r'burialpermit', burialPermit.BurialPermitViewset, 'burialpermit')
router.register(r'sector', sector.SectorViewset, 'sector')
router.register(r'periodicity', periodicity.PeriodicityViewset, 'periodicity')
router.register(r'parcel', parcel.ParcelViewset, 'parcel')
router.register(r'grave', grave.GraveViewset, 'grave')
router.register(r'tax', tax.TaxViewset, 'tax')
router.register(r'payment', payment.PaymentViewset, 'payment')


urlpatterns = [
    path('', include(router.urls))
]

