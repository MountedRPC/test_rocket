from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/factory/', include('factory.urls')),
    # path('api/v1/retailnetwork/', include('retailnetwork.urls')),
    # path('api/v1/indentrepreneur/', include('indentrepreneur.urls')),
    path('api/v1/dealership/', include('dealership.urls')),
    # path('api/v1/distributor/', include('distributor.urls')),
]
