from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from user.models import *
from weeklyCalendar import models as calendar_models
import datetime, pprint, csv


class FamilyStats(generic.ListView):
    template_name = 'family_stats.html'
    model = Signup



    def get(self, request, *args, **kwargs):
        weekly_timedelta = self.week_hours(datetime.date.today(), Family.objects.get(user=self.request.user))
        weekly_hours = weekly_timedelta.total_seconds() // 3600
        weekly_minutes = (weekly_timedelta.total_seconds() - (weekly_hours * 3600)) // 60
        self.week_total = str(weekly_hours) + "h " + str(weekly_minutes) + "m"

        monthly_timedelta = self.month_hours(datetime.date.today(), Family.objects.get(user=self.request.user))
        monthly_hours = monthly_timedelta.total_seconds() // 3600
        monthly_minutes = (monthly_timedelta.total_seconds() - (monthly_hours * 3600)) // 60
        self.month_total = str(monthly_hours) + "h " + str(monthly_minutes) + "m"

        self.required_hours = self.required_hours(Family.objects.get(user=self.request.user))
        self.current_signups = self.current_signups(Family.objects.get(user=self.request.user))
        return render(request, self.template_name, {'view':self})



    """ Using the current date it gets the entire weeks hours for selected family.
        Return:
            total: a timedelta object of the current hours and minutes volunteered that week.
        Parameters: 
            requested_week: is the week you would like the volunteer hours for.
                It must be a datetme.date object of a single day in the requested week.
            requested_family: is the family that you want the weekly hours for.
                It must be a single Family object (from user.models) 
    """
    def week_hours(self, requested_week, requested_family):
        week = requested_week
        offset = week.weekday()
        # Gets the beginning and end dates based on current date
        begin_week =  week - datetime.timedelta(days=offset)
        end_week = week + datetime.timedelta(days=(6 - offset))
        family = requested_family
        signups = Signup.objects.filter(volunteer__family__familyID = family.familyID, 
                                        date__range=(begin_week, end_week))

        # Goes through each signup for the family and calculates total hours for the week
        total = datetime.timedelta(hours=0)
        for day in signups:
            end = datetime.timedelta(hours=day.end_time.hour,minutes=day.end_time.minute)
            start = datetime.timedelta(hours=day.start_time.hour,minutes=day.start_time.minute)
            time_slots = calendar_models.TimeSlot.objects.all()
            for ts in time_slots:
                if ts.multiplier != 1:
                    ts_start_td = datetime.timedelta(hours=ts.start.hour, minutes=ts.start.minute)
                    ts_end_td = datetime.timedelta(hours=ts.end.hour, minutes=ts.end.minute)
                    if ts_start_td < end and ts_end_td > start:
                        if ts_end_td > end:
                            to_mult = end - ts_start_td
                        else:
                            to_mult = ts_end_td - start
                        mult = to_mult * ts.multiplier
                        total -= to_mult
                        total += mult

            total = total + (end - start)

        

        transfers_from = TimeTransfer.objects.filter(from_family = family,
                                                    date__range=(begin_week, end_week))
        transfers_to = TimeTransfer.objects.filter(to_family = family,
                                                    date__range=(begin_week, end_week))

        for transfer in transfers_from:
            td = datetime.timedelta(hours=transfer.time.hour, minutes=transfer.time.minute)
            total -= td
        for transfer in transfers_to:
            td = datetime.timedelta(hours=transfer.time.hour, minutes=transfer.time.minute)
            total += td

        return total





    """ Using the requested date it gets the entire month hours for selected family.
        Return:
            total: a timedelta object of the current hours and minutes volunteered that month.
        Parameters: 
            requested_month: is the month you would like the volunteer hours for.
                It must be a datetme.date object of a single day in the requested month.
            requested_family: is the family that you want the monthly hours for.
                It must be a single Family object (from user.models)
    """
    def month_hours(self, requested_month, requested_family):
        current = requested_month
        family = requested_family
        signups = Signup.objects.filter(volunteer__family__familyID = family.familyID, 
                                        date__year=current.year, date__month=current.month)
        # Goes through each signup for the family and calculates total hours for the month
        total = datetime.timedelta(hours=0, minutes=0)
        for day in signups:
            end = datetime.timedelta(hours=day.end_time.hour,minutes=day.end_time.minute)
            start = datetime.timedelta(hours=day.start_time.hour,minutes=day.start_time.minute)
            time_slots = calendar_models.TimeSlot.objects.all()
            for ts in time_slots:
                if ts.multiplier != 1:
                    ts_start_td = datetime.timedelta(hours=ts.start.hour, minutes=ts.start.minute)
                    ts_end_td = datetime.timedelta(hours=ts.end.hour, minutes=ts.end.minute)
                    if ts_start_td < end and ts_end_td > start:
                        if ts_end_td > end:
                            to_mult = end - ts_start_td
                        else:
                            to_mult = ts_end_td - start
                        mult = to_mult * ts.multiplier
                        total -= to_mult
                        total += mult

            total = (total + (end - start))


        transfers_from = TimeTransfer.objects.filter(from_family = family,
                                                    date__year = current.year,
                                                    date__month = current.month)
        transfers_to = TimeTransfer.objects.filter(to_family = family,
                                                    date__year = current.year,
                                                    date__month = current.month)
        for transfer in transfers_from:
            td = datetime.timedelta(hours=transfer.time.hour, minutes=transfer.time.minute)
            total -= td
        for transfer in transfers_to:
            td = datetime.timedelta(hours=transfer.time.hour, minutes=transfer.time.minute)
            total += td

        return total 



    """ This functions return the required hours a family must complete depending on how many children they have. 
        Return:
            hours: an int/float of the amount of hours the family must complete
        Parameters:
            requested_family: is the family that you want the number of children for.
                It must be a single Family object (from user.models)
    """
    def required_hours(self, requested_family):
        children = (Child.objects.filter(family__familyID = requested_family.familyID).count())
        if (children < 1):
            hours = 0
        elif (children == 1):
            hours = 2.5
        else:
            hours = 5

        return hours


    '''  This shows all future signups for a specific family
        Return:
            signups: A query set of Signup objects that will occur in the future
        Parameters:
            requested_family: is the family that you want the number of children for.
                It must be a single Family object (from user.models)
    '''
    def current_signups(self, requested_family):
        day = datetime.date.today()
        signups = Signup.objects.filter(volunteer__family__familyID = requested_family.familyID, 
            date__gte=day).order_by('date')
        return signups



class AdminStats(generic.ListView):
    template_name = "admin_stats.html"
    model = Signup


    def __init__(self):
        self.admin_stats = self.all_family_stats(datetime.date.today())
        self.date = (datetime.date.today().strftime("%B"), datetime.date.today().strftime("%Y"))



    ''' Using a queryset of signups determine the total time spent volunteering
        Return:
            total: a timedelta object with the hours and minutes spent volunteering
        Parameters:
            signup_query: a queryset of Signup objects (from user.Models) that you want to count the time for
    '''
    def total_hours(self, signup_query):
        total = datetime.timedelta(hours=0)
        for day in signup_query:
            end = datetime.timedelta(hours=day.end_time.hour,minutes=day.end_time.minute)
            start = datetime.timedelta(hours=day.start_time.hour,minutes=day.start_time.minute)
            total = total + (end - start)
        return total



    """ This functions return the required hours a family must complete depending on how many children they have. 
        Return:
            hours: an int/float of the amount of hours the family must complete
        Parameters:
            requested_family: is the family that you want the number of children for.
                It must be a single Family object (from user.models)
    """
    def required_hours(self, requested_family):
        children = (Child.objects.filter(family__familyID = requested_family.familyID).count())
        if (children < 1):
            hours = 0
        elif (children == 1):
            hours = 2.5
        else:
            hours = 5

        return hours




    """ Using the requested date it gets the all stats admins need for selected family.
        Return:
            family_stats: A dictionary with specific info on each family
            ex. family_stats{ fam_name : string, volunteer1 : string, volunteer2 : string, 
                wk1 : datetime.timedelta, wk2 : datetime.timedelta, wk3 : datetime.timedelta, 
                wk4 : datetime.timedelta, month_hours : datetime.timedelta, 
                month_total : datetime.timedelta, year_total : datetime.timedelta }
        Parameters: 
            requested_month: is the month you would like the volunteer hours for.
                It must be a datetme.date object of a single day in the requested month.
            requested_family: is the family that you want the monthly hours for.
                It must be a single Family object (from user.models)
    """
    def single_family_stats(self, requested_month, requested_family):
        family_stats = {"fam_name" : requested_family.family_name}
        volunteer_query = Volunteer.objects.filter(family__familyID = requested_family.familyID).order_by('volunteerID')

        # This block adds the first (and possibly second) volunteer in the family as the main facilitators for the family (aka parents)
        if (volunteer_query.count() == 1):
            family_stats['volunteer1'] = volunteer_query[0].first_name
            family_stats['volunteer2'] = ""
        elif(not volunteer_query.exists()):
            family_stats['volunteer1'] = ""
            family_stats['volunteer2'] = ""
        else:
            family_stats['volunteer1'] = volunteer_query[0].first_name
            family_stats['volunteer2'] = volunteer_query[1].first_name

        # This block adds the first week of signups to the dictionary
        start_wk = datetime.date(requested_month.year, requested_month.month, 1)
        end_wk = datetime.date(requested_month.year, requested_month.month, 7)
        wk_query = Signup.objects.filter(volunteer__family__familyID = requested_family.familyID, 
                                        date__range=(start_wk, end_wk))
        family_stats['wk1'] = self.total_hours(wk_query)
        # This block adds the second week of signups to the dictionary
        start_wk = datetime.date(requested_month.year, requested_month.month, 8)
        end_wk = datetime.date(requested_month.year, requested_month.month, 14)
        wk_query = Signup.objects.filter(volunteer__family__familyID = requested_family.familyID, 
                                        date__range=(start_wk, end_wk))
        family_stats['wk2'] = self.total_hours(wk_query)
        # This block adds the third week of signups to the dictionary
        start_wk = datetime.date(requested_month.year, requested_month.month, 15)
        end_wk = datetime.date(requested_month.year, requested_month.month, 21)
        wk_query = Signup.objects.filter(volunteer__family__familyID = requested_family.familyID, 
                                        date__range=(start_wk, end_wk))
        family_stats['wk3'] = self.total_hours(wk_query)
        # This block adds the fourth week of signups to the dictionary
        start_wk = datetime.date(requested_month.year, requested_month.month, 22)
        end_wk = datetime.date(requested_month.year, requested_month.month, 28)
        wk_query = Signup.objects.filter(volunteer__family__familyID = requested_family.familyID, 
                                        date__range=(start_wk, end_wk))
        family_stats['wk4'] = self.total_hours(wk_query)
        
        # Adds the monthly hours of the family to the dictionary
        monthly_hours = getattr(FamilyStats(), 'month_hours')
        family_stats['month_hours'] = monthly_hours(requested_month, requested_family)

        # Adds month total (above or below required) to the dictionary)
        required = self.required_hours(requested_family) * 4
        family_stats['month_total'] = (family_stats['month_hours'] - datetime.timedelta(hours=required))

        # Adds the yearly total of hours
        signup_query = Signup.objects.filter(volunteer__family__familyID = requested_family.familyID, 
                                        date__year=requested_month.year)
        hours = self.total_hours(signup_query)
        required = (self.required_hours(requested_family) * 40)
        family_stats['year_total'] = (self.total_hours(signup_query) - datetime.timedelta(hours=required))

        return family_stats




    ''' Goes through all family accounts and gets all the stats for them
        Return:
            all_family_stats: a list of dictionaries were each dictionary is a single family's stats
        Parameters:
            requested_month: the month you want all the stats for. 
            It must be a datetime object of a single day in the month.
    '''
    def all_family_stats(self, requested_month):
        all_stats = []
        families = Family.objects.all()
        for fam in families:
            if fam.user.is_superuser == 0:
                all_stats.append(readable_format(self.single_family_stats(requested_month, fam)))
        return all_stats




    ''' This function allows for the download of all the family stats as a csv file for use in excel
        Return:
            response: an HttpResponse containing the csv file with data
    '''
    def post(self, request, *args, **kwargs):
        if 'csv' in request.POST:
            pprint.pprint(request.POST)
            func = AdminStats()
            requested_month = datetime.date(month=int(request.POST['month']), year=int(request.POST['year']), day=1)
            all_stats = []
            families = Family.objects.all()
            for fam in families:
                all_stats.append(func.single_family_stats(requested_month, fam))
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="{:%B %Y stats.csv}"'.format(requested_month)

            w = csv.writer(response)
            w.writerow(['Family Name', 'Volunteer 1', 'Volunteer 2', 'Week 1', 'Week 2',
                        'Week 3', 'Week 4', 'Month Hours', 'Month Total', 'Year Total'])
            for fam in all_stats:
                w.writerow(readable_format(fam))
            return response



''' Takes a dictionary and sets each entry to the correct location in a list
    Return: 
        out_list: a list with all entries from the dictionary, but ordered
    Parameters:
        entry: a dictionary object containing the stats for a single family.
'''
def readable_format(entry):
    out_list = []
    out_list.append(entry['fam_name'])
    out_list.append(entry['volunteer1'])
    out_list.append(entry['volunteer2'])
    out_list.append(format((entry['wk1']).total_seconds() / 3600, '.2f'))
    out_list.append(format((entry['wk2']).total_seconds() / 3600, '.2f'))
    out_list.append(format((entry['wk3']).total_seconds() / 3600, '.2f'))
    out_list.append(format((entry['wk4']).total_seconds() / 3600, '.2f'))
    out_list.append(format((entry['month_hours']).total_seconds() / 3600, '.2f'))
    out_list.append(format((entry['month_total']).total_seconds() / 3600, '.2f'))
    out_list.append(format((entry['year_total']).total_seconds() / 3600, '.2f'))
    return out_list













