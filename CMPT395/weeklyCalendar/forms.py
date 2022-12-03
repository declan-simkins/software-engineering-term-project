from django import forms
from user.models import Signup as SignUp
from . import models

class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ("start_time", "end_time",)
    
class TimeSlotForm(forms.ModelForm):

    class Meta:
        model = models.TimeSlot
        fields = ("title", "start", "end", "multiplier")

class ClassroomForm(forms.ModelForm):
    
    class Meta:
        model = models.Classroom
        fields = ("title", "color")