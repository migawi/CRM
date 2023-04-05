from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import homeview, about
from userprofile.views import signup
from dashboard.views import dashboard

urlpatterns = [
    path('', homeview, name='home'),
    path('about/', about, name='about'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('crmclient.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

