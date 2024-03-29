from django.urls import path, include

from rest_framework.routers import DefaultRouter

from jobhunter_api import views

router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('openings',views.OpeningsViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]