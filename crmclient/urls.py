from django.urls import path

from . import views

urlpatterns = [
    path('', views.client_catalog, name='clients'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('<int:pk>/delete/', views.delete_clients, name='delete_clients'),
    path('new_client/', views.new_client, name='newclient'),
    path('<int:pk>/new-comment/', views.client_detail, name='addcomment'),
    path('<int:pk>/edit/', views.edit_clients, name='edit_clients'),
]