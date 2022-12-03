# Django Imports
from django import template

# Python Imports
import datetime

# App Imports
from user import models as user_models
from stats import views as stats_views

register = template.Library()

@register.simple_tag
def format_time(time):
  return time.__format__("%H:%M")

@register.simple_tag
def format_date(date):
  return date.__format__("%Y-%m-%d")

@register.simple_tag
def comp(str1, str2):
  if str1 == str2:
    return "true"
  else:
    return "false"

@register.simple_tag
def user_match(volunteer, view):
  if volunteer.family.user == view.request.user:
    return True
  else:
    return False

@register.simple_tag
def to_lower(str):
  return str.lower()

@register.simple_tag
def weekly_hours(view):
  family = user_models.Family.objects.get(user=view.request.user)
  day = datetime.date.today()
  weekly_td = stats_views.FamilyStats.week_hours(view, day, family)
  weekly_hours = weekly_td.total_seconds() // 3600
  weekly_minutes = (weekly_td.total_seconds() - (weekly_hours * 3600)) // 60
  return str(weekly_hours) + "h, " + str(weekly_minutes) + "m"

@register.simple_tag
def monthly_hours(view):
  family = user_models.Family.objects.get(user=view.request.user)
  day = datetime.date.today()
  weekly_td = stats_views.FamilyStats.month_hours(view, day, family)
  weekly_hours = weekly_td.total_seconds() // 3600
  weekly_minutes = (weekly_td.total_seconds() - (weekly_hours * 3600)) // 60
  return str(weekly_hours) + "h, " + str(weekly_minutes) + "m"