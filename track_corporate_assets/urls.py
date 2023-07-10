
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('assets.urls'), name='asset_api')
]
