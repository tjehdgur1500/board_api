from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import CardViewSet, UserViewSet

router = SimpleRouter()
router.register(r'cards', CardViewSet)
router.register(r'cards/<int:pk>/', CardViewSet)
router.register(r'users', UserViewSet)
router.register(r'users/<int:pk>/', UserViewSet)


urlpatterns = router.urls
