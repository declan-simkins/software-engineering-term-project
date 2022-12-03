from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import MyUser
from user.models import TimeTransfer 

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'is_superuser', 'is_staff', 'email']

class EditUserForm(forms.ModelForm):
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ['username', 'is_superuser', 'email']

class TimeTransferForm(forms.ModelForm):

    class Meta:
        model = TimeTransfer
        fields = ('to_family', 'time')
