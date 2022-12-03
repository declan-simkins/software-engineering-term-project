from django import forms
from .models import *
from user.models import Volunteer
import datetime


CLASSES = [ ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')]


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateFieldTripForm(forms.ModelForm):

    class Meta:
        model = FieldTrip
        fields = ('location', 'title', 'classes', 'info', 'date')
        current = datetime.date.today()
        widgets = {'date' : DateInput()}
        queryset = FieldTrip.objects.filter(date__gte=current)



class SignupFieldTripForm(forms.ModelForm):

    class Meta:
        model = FieldTripSignup
        fields = ('trip', 'volunteer')