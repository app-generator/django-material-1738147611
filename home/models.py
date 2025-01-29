# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Devices(models.Model):

    #__Devices_FIELDS__
    device_name = models.CharField(max_length=255, null=True, blank=True)
    port = models.CharField(max_length=255, null=True, blank=True)
    slave_id = models.IntegerField(null=True, blank=True)
    baud_rate = models.IntegerField(null=True, blank=True)
    word_length = models.IntegerField(null=True, blank=True)
    parity = models.CharField(max_length=255, null=True, blank=True)
    stop_bits = models.IntegerField(null=True, blank=True)
    function_code = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Devices_FIELDS__END

    class Meta:
        verbose_name        = _("Devices")
        verbose_name_plural = _("Devices")


class Devicetags(models.Model):

    #__Devicetags_FIELDS__
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    tag_names = models.TextField(max_length=255, null=True, blank=True)

    #__Devicetags_FIELDS__END

    class Meta:
        verbose_name        = _("Devicetags")
        verbose_name_plural = _("Devicetags")


class Dashboards(models.Model):

    #__Dashboards_FIELDS__
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)
    dashboard_name = models.CharField(max_length=255, null=True, blank=True)
    dashboard_description = models.TextField(max_length=255, null=True, blank=True)

    #__Dashboards_FIELDS__END

    class Meta:
        verbose_name        = _("Dashboards")
        verbose_name_plural = _("Dashboards")


class Widgets(models.Model):

    #__Widgets_FIELDS__
    dashboard = models.ForeignKey(Dashboards, on_delete=models.CASCADE)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    widget_name = models.CharField(max_length=255, null=True, blank=True)

    #__Widgets_FIELDS__END

    class Meta:
        verbose_name        = _("Widgets")
        verbose_name_plural = _("Widgets")



#__MODELS__END
