from django import forms
from .models import TimeOffRequest
from user.models import Volunteer, Family


class DateInput(forms.DateInput):
    input_type = 'date'

class RequestTimeOffForm(forms.ModelForm):
    def __init__(self, family = None, **kwargs):
        super().__init__(**kwargs)
        self.family = family

    def save(self, commit=True):
        form_object = super(RequestTimeOffForm, self).save(commit=False)
        form_object.family = self.family
        if(commit):
            form_object.save()
        return form_object

    class Meta:
        model = TimeOffRequest
        fields = ( 'start_date', 'end_date','reason_for_time_off',)
        widgets = {'start_date':DateInput(), 'end_date':DateInput()}