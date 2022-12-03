from django.urls import path, include

from . import views

urlpatterns = [
    path('create/', views.CreateFieldTrip.as_view(), name="create_field_trip"),
    path('', views.CurrentTrip.as_view(), name="view_field_trip"),
]