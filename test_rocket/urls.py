from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Part №1
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/factory/', include('factory.urls')),
    path('api/v1/retailnetwork/', include('retailnetwork.urls')),
    path('api/v1/indentrepreneur/', include('indentrepreneur.urls')),
    path('api/v1/dealership/', include('dealership.urls')),
    path('api/v1/distributor/', include('distributor.urls')),
    # Part №2
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
