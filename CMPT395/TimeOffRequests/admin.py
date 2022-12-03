from django.contrib import admin
from .models import TimeOffRequest

def set_status_to_approved(modeladmin, request, queryset):
    queryset.update(status = 'a')
set_status_to_approved.short_description = "Approve time off request"

def set_status_to_denied(modeladmin, request, queryset):
    queryset.update(status = 'd')
set_status_to_denied.short_description = "Deny time off request"

def set_status_to_pending(modeladmin, request, queryset):
    queryset.update(status = 'p')
set_status_to_pending.short_description = "Set time off request to 'Pending'"

class TimeOffRequestAdmin(admin.ModelAdmin):
    list_display = ('family', 'start_date', 'end_date', 'status',)
    actions = [set_status_to_approved, set_status_to_denied, set_status_to_pending]



# Register your models here.
admin.site.register(TimeOffRequest, TimeOffRequestAdmin)
