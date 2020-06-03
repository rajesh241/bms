from django.contrib import admin
from baseapp.models import PhoneCall
# Register your models here.
class PhoneCallModelAdmin(admin.ModelAdmin):
    """Model Adminf or class Location"""
    list_display = ["id", "phone", "status"]
    list_filter = ["in_progress", "is_complete"]

admin.site.register(PhoneCall, PhoneCallModelAdmin)
