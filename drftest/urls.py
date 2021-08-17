from rest_framework import routers

from drftest.views import TestModelViewSet

router = routers.SimpleRouter()
router.register(r'testmodels', TestModelViewSet)
urlpatterns = router.urls