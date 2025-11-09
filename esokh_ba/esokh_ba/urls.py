from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from esokhapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'orshinsuus', views.OrshinsuuViewSet)
router.register(r'tulburs', views.TulburViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'sanals', views.SanalViewSet)
router.register(r'sohs', views.SohViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login', views.login_view, name='login'),  # <- энд trailing slash байна
]
