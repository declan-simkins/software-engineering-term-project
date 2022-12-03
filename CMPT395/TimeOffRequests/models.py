from django.db import models
from user.models import Family

class TimeOffRequest(models.Model):
    STATUS_CHOICES = (
        ('a', 'Approved'),
        ('d', 'Denied'),
        ('p', 'Pending'),
    )
    
    family = models.ForeignKey(Family, on_delete = models.CASCADE, null=True)
    start_date = models.DateField(blank = False)
    end_date = models.DateField(blank = False)
    reason_for_time_off = models.TextField(max_length = 300)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'p')

    def __str__(self):
        return "TimeOffRequest|" + "Family:" + str(self.family) + " Start date:" + str(self.start_date) +\
         "| End Date:" + str(self.end_date) + "| Status:" + str(self.status) + "\n"
