from django.template.defaulttags import register
from pytz import timezone
from datetime import datetime


@register.filter
def adjust_time_zone(date, tz):
    return date.astimezone(timezone(tz)).replace(tzinfo=None)
