from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models
from django.conf import settings
import pprint


class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    objects = MyUserManager()


''' 
This class extends Django's existing User info using MyUser
'''
class Family(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    familyID = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    current_volunteer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.family_name)



class Child(models.Model):
    childID = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    classroom = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Volunteer(models.Model):
    volunteerID = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)


    def getCurrent(view):
        family = Family.objects.get(user=view.request.user)
        return Volunteer.objects.get(volunteerID=family.current_volunteer)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class Signup(models.Model):
    signupID = models.AutoField(primary_key=True)
    date = models.DateField(["%Y-%m-%d"], blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=15)
    volunteer = models.ForeignKey(Volunteer, blank=True, null=True, on_delete= models.CASCADE)

    def __str__(self):
        return ("Date: " + str(self.date) + " Start: " + str(self.start_time) + " End: " + str(self.end_time) + " Volunteer: " + str(self.volunteer))

    def double_booked(view, new_signup):
        fam = Family.objects.get(user=view.request.user)
        vol = Volunteer.objects.get(volunteerID=fam.current_volunteer)
        middle_signups = Signup.objects.filter(volunteer__volunteerID=vol.volunteerID, date=new_signup.date, start_time__lte=new_signup.start_time, end_time__gte=new_signup.start_time)
        before_signups = Signup.objects.filter(volunteer__volunteerID=vol.volunteerID, date=new_signup.date, start_time__gte=new_signup.start_time, start_time__lte=new_signup.end_time)
        if middle_signups or before_signups:
            return True
        return False


class TimeTransfer(models.Model):
    timetransferID = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField()
    from_family = models.ForeignKey(Family, related_name="%(class)s_from_family", on_delete=models.CASCADE)
    to_family = models.ForeignKey(Family, related_name="%(class)s_to_family", on_delete=models.CASCADE)
    
    def __str__(self):
        return ("Transfered " + self.time.__str__() + " from family \"" + self.from_family.__str__() + "\" to family \"" + self.to_family.__str__() + "\".\n")