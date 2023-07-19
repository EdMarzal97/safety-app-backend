from django.urls import path, include
from rest_framework import routers
from safetyapi import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
