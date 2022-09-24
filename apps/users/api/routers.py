from rest_framework.routers import DefaultRouter

from apps.users.api.views.user_views import UserViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = router.urls