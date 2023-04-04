from django.conf import settings
from django.contrib import admin
from django.urls import path

from core.views import homeview, about

urlpatterns = [
    path('', homeview, name='home'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

