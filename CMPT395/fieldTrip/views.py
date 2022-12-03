from django import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import *
from user.models import *
import datetime



class CreateFieldTrip(CreateView):
    form_class = CreateFieldTripForm
    success_url = reverse_lazy('create_field_trip')
    template_name = "field_trip.html"



class CurrentTrip(ListView):
    model = FieldTrip
    template_name = 'current_field_trips.html'

    def get(self, request):
        field_trips = FieldTrip.objects.filter(date__gte=datetime.date.today())
        field_trip_signups = FieldTripSignup.objects.all()


        return render(request, self.template_name, {'field_trips':field_trips, 'field_trip_signups':field_trip_signups, 'view':self})
    
    def post(self, request):
        if('add_to_field_trip' in request.POST):
            add_volunteer = Volunteer.objects.get(volunteerID=Volunteer.getCurrent(self).volunteerID)
            field_trip_id = request.POST.get("add_to_field_trip")
            
            if(FieldTripSignup.objects.filter(trip=FieldTrip.objects.get(id=field_trip_id), volunteer=add_volunteer).exists()):
                return redirect(reverse('view_field_trip'))
            else:
                FieldTripSignup.objects.create(trip=FieldTrip.objects.get(id=field_trip_id), volunteer=add_volunteer)
                return redirect(reverse('view_field_trip'))
        
        elif('delete_field_trip_signup' in request.POST):
            delete_signup_field_trip_id = request.POST.get("delete_field_trip_signup")
            if(FieldTripSignup.objects.filter(trip=FieldTrip.objects.get(id=delete_signup_field_trip_id), volunteer = Volunteer.objects.get(volunteerID=Volunteer.getCurrent(self).volunteerID)).exists()):
                FieldTripSignup.objects.get(trip=FieldTrip.objects.get(id=delete_signup_field_trip_id), volunteer = Volunteer.objects.get(volunteerID=Volunteer.getCurrent(self).volunteerID)).delete()
                return redirect(reverse('view_field_trip'))
            else:
                return redirect(reverse('view_field_trip'))
        elif('delete_field_trip' in request.POST):
            delete_field_trip_id = request.POST.get("delete_field_trip")
            if(FieldTripSignup.objects.filter(trip=FieldTrip.objects.get(id=delete_field_trip_id)).exists()):
                signup_list = FieldTripSignup.objects.filter(trip=FieldTrip.objects.get(id=delete_field_trip_id))
                for signup in signup_list:
                    signup.delete()
                FieldTrip.objects.get(id=delete_field_trip_id).delete()
                return redirect(reverse('view_field_trip'))
            else:
                FieldTrip.objects.get(id=delete_field_trip_id).delete()
                return redirect(reverse('view_field_trip'))

            


# Needs work
class SignupFieldTrip(CreateView):
    form_class = SignupFieldTripForm
    success_url = reverse_lazy('signup_field_trip')
    template_name = 'signup_field_trip.html'



    



