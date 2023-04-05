from django.urls import path

from . import views

urlpatterns = [
    path('', views.leads_catalog, name='leads'),
    path('<int:pk>/', views.leads_detail, name='leadsdetail'),
    path('<int:pk>/edit/', views.edit_lead, name='editleads'),
    path('<int:pk>/delete/', views.delete_lead, name='deleteleads'),
    path('<int:pk>/convert/', views.convert_to_client, name='convert_to_client'),
    path('new-lead/', views.new_lead, name='newlead'),
]