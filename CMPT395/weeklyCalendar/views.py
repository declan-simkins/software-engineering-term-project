from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignUpForm
from user.models import Signup as SignUp
from user.models import Family, Volunteer
from . import models

import calendar
import datetime as dt

# Create your views here.
class WeeklyCalendarView(TemplateView):
  # Djagno variables
  template_name = "calendar.html"
  signup_form = SignUpForm
  signup_objects = SignUp.objects.all()
  
  class TimeSlot:
    def __init__(self, init_title, init_start, init_end):
      self.title = init_title
      self.start = init_start
      self.end = init_end
    # End init
  # End TimeSlot  
  
  # Constants
  WEEK_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday"
               , "Thursday", "Friday", "Saturday"]
  
  
  def __init__(self):
    self.CLASSROOMS = models.Classroom.objects.all().order_by('title')
    self.TIME_SLOTS = models.TimeSlot.objects.all().order_by('start')
    self.current_date = dt.datetime.now()
    self.date_and_name = self.pair_date_name(self.WEEK_DAYS, self.get_week(self.current_date))
    self.signup_objects = SignUp.objects.all()
  
  def post(self, request, *args, **kwargs):
    if 'prev-week' in request.POST:
      date_raw = request.POST.get("prev-week").split('-')
      date = dt.date(int(date_raw[0]), int(date_raw[1]), int(date_raw[2])) - dt.timedelta(7)
      self.date_and_name = self.pair_date_name(self.WEEK_DAYS, self.get_week(date))
    
    elif 'next-week' in request.POST:
      date_raw = request.POST.get("next-week").split('-')
      date = dt.date(int(date_raw[0]), int(date_raw[1]), int(date_raw[2])) + dt.timedelta(7)
      self.date_and_name = self.pair_date_name(self.WEEK_DAYS, self.get_week(date))
    
    elif 'delete-signup' in request.POST:
      sid = request.POST.get("delete-signup")
      SignUp.objects.get(signupID=sid).delete()

    else:
      form = self.signup_form(request.POST)
      if form.is_valid():
        su = form.save(commit=False)
        # Automated fields go here
        su.classroom = request.POST.get("classroom")
        su.date = request.POST.get("day", default="DEFAULT")
        su.volunteer = Volunteer.getCurrent(self)
        if (SignUp.double_booked(self, su)):
            return render(request, self.template_name, {'view' : self, 'double_booked' : True})
        su.save()
        self.signup_objects = SignUp.objects.all()
        return render(request, self.template_name, {'view' : self, 'success' : True})
      else:
        return render(request, self.template_name, {'view' : self, 'success' : False})
    return render(request, self.template_name, {'view' : self})

  def get_week(self, date):
    """ Returns the week of date represented by datetime objects
        Pre: None
        Post: None
        Parameters: None
        Return: List of 7 datetime objects representing the current week
    """
    # Get this month's calendar with the first day of the week as Sunday
    #   hence calendar.Calendar(6)
    month = calendar.Calendar(6).monthdatescalendar(date.year, date.month)
    for week in month:
      for day in week:
        if date.day == day.day and date.month == day.month:
          return week

  def pair_date_name(self, week_days, dates):
    """ Creates and returns list of tuples (string weekday, datetime date)
        Pre: week_days and dates are populated & ordered lists of strings and
          datetimes
        Post: None
        Param: week_days: Ordered list of string week day names
          e.g. ("Sunday", "Monday", etc.);
          dates: Ordered list of datetime objects;
          week_days and dates should be parallel
            (i.e. The first day in week_days should correspond to the first
            day in dates)
        Return: List of tuples of paired day names and datetimes
    """
    day_name = []
    for i in range(len(dates)):
      day_name.append((week_days[i], dates[i]))
    return day_name[1:-1] # Work week [Monday - Friday]

class SignupView(TemplateView):
  template_name = "signups.html"
  signup_model = SignUp
  signup_objects = SignUp.objects.all()
  
  def get(self, request, *args, **kwargs):
    signup_objects = SignUp.objects.all()
    return render(request, self.template_name, {'view' : self, 'sign_up_objects': signup_objects})
