from django.template.defaulttags import register
from datetime import datetime, timezone


@register.simple_tag
def remain_time(my_time):
    return str(my_time - datetime.now(timezone.utc))


@register.filter
def capitalize_title(title):
    return title.title()

