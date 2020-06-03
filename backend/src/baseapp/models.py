from django.db import models
from django_mysql.models import JSONField

# Create your models here.



class PhoneCall(models.Model):
    """This is the basic Model for Phone Call"""
    phone = models.CharField(max_length=11)
    status = models.CharField(max_length=256, default="inQueue")
    in_progress = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    retry = models.PositiveSmallIntegerField(default=0)
    sid = models.CharField(max_length=256, null=True, blank=True)
    vendor_status = models.CharField(max_length=256, null=True, blank=True)
    exotel_app_no = models.CharField(max_length=256, null=True, blank=True)
    extra_fields = JSONField(null=True, blank=True)  # requires Django-Mysql package
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """To define meta data attributes"""
        db_table = 'phonecall'
    def __str__(self):
        """Default str method for the class"""
        return f"{self.phone}-{self.status}"


