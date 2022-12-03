from django.urls import path, include

from . import views

urlpatterns = [
  path('signupTest/', views.SignupView.as_view(), name='signupTest'),
  path('', views.WeeklyCalendarView.as_view(), name='weeklyCalendar'),
]
