from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/profile/',include('profile_app.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # access & refresh token from path('o/token/') along with client_id and grant type
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
