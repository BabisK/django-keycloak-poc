from rest_framework import routers

from perm.views import SongModelViewSet

router = routers.SimpleRouter()
router.register(r'songs', SongModelViewSet)
urlpatterns = router.urls