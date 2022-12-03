from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import RequestTimeOffForm
from django.urls import reverse
from .models import TimeOffRequest
from user.models import Volunteer, Family
import datetime

# Create your views here.

class TimeOffRequestView(TemplateView):
    template_name = 'time_off_request.html'
    
    def display_status(self, letter):
        if(letter.lower() == "a"):
            return "Approved"
        elif(letter.lower() == "p"):
            return "Pending"
        else:
            return "Denied"


    def get(self, request):
        request_time_off_form = RequestTimeOffForm()
        current_time_off_requests = TimeOffRequest.objects.filter(family = Volunteer.getCurrent(self).family, end_date__gte=datetime.date.today())
        
        for x in current_time_off_requests:
            x.status = self.display_status(x.status)

        return render(request, self.template_name, {'request_time_off_form':request_time_off_form, "time_off_requests" : current_time_off_requests, 'view':self})
    
    def post(self, request):
        if('delete-time-off-request' in request.POST):
            del_time_off_request = request.POST.get("delete-time-off-request")
            TimeOffRequest.objects.get(id = del_time_off_request).delete()
            return redirect(reverse('request_time_off'))

        else:
            request_time_off_form = RequestTimeOffForm(data = request.POST, family = Volunteer.getCurrent(self).family)
            if(request_time_off_form.is_valid()):
                request_time_off_form.save()
                return redirect(reverse('request_time_off'))
            
            return render(request, self.template_name, {'request_time_off_form':request_time_off_form, 'view':self})
    
