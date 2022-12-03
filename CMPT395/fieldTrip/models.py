from django.db import models
from user.models import Volunteer


class FieldTrip(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    info = models.TextField(max_length=500)
    classes = models.CharField(max_length=50, default="Enter Classes Here")
    date = models.DateField()

    def __str__(self):
        return self.title


class FieldTripSignup(models.Model):
    trip = models.ForeignKey(FieldTrip, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, unique=False)

    def __str__(self):
        return "%s %s" % (self.trip, self.volunteer)



