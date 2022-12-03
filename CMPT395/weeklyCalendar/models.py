from django.db import models

class TimeSlot(models.Model):
    timeslotID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    start = models.TimeField()
    end = models.TimeField()
    multiplier = models.FloatField(default=1)

    def __str__(self):
        return self.title + '\n' + self.start + '-' + self.end

class Classroom(models.Model):
    classroomID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.title
