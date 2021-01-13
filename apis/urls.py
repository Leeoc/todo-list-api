from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'app'
router = DefaultRouter()
router.register('', views.TodoViewSet, basename='todos')

urlpatterns = [
    path('todo/', include(router.urls))
]
