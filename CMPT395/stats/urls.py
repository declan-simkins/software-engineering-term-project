from django.urls import path, include

from . import views

urlpatterns = [
    path('family/', views.FamilyStats.as_view(), name='family_stats'),
    path('admin/', views.AdminStats.as_view(), name='admin_stats'),
]
