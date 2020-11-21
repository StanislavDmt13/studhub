from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("backend.urls"), name="api"),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include('frontend.urls')),
]
