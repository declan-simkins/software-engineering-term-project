from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import MyUserCreationForm
from . models import MyUser, Family, Child, Volunteer, Signup

class FamilyInline(admin.TabularInline):
    model = Family
    fields = ('user', 'family_name', 'phone', 'email')

class VolunteerInline(admin.TabularInline):
    model = Volunteer

class ChildInline(admin.TabularInline):
    model = Child

class MyUserAdmin(admin.ModelAdmin):
    model = MyUser
    fields = ('username', 'password', 'is_superuser', 'is_active')
    inlines = [
        FamilyInline,
    ]
    
class FamilyAdmin(admin.ModelAdmin):
  list_display = ('user', 'familyID', 'family_name')
  inlines = [
      VolunteerInline,
      ChildInline,
  ]

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("volunteerID", "first_name")

class ChildAdmin(admin.ModelAdmin):
    list_display = ("childID", "family", "first_name")

class SignupAdmin(admin.ModelAdmin):
    list_display = ('signupID', 'date', 'start_time', 'end_time', 'volunteer')

    
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Signup, SignupAdmin)