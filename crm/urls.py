from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('contacts/add/', views.add_contact_view, name='add_contact'),
    path('contacts/<int:pk>/edit/', views.edit_contact_view, name='edit_contact'),
    path('contacts/<int:pk>/delete/', views.delete_contact_view, name='delete_contact'),
]
