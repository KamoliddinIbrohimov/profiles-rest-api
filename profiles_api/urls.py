from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views
from .views import HelloApiView, UserLoginApiView, UserProfileFeedViewSet

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
