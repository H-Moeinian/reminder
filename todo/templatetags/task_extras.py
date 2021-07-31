from time import strftime

from django.template.defaulttags import register
from datetime import datetime, timezone


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def make_title(title):
    return str(title).title()


@ register.filter
def task_done(done):
    return "Yes" if done else "No"


@register.simple_tag
def my_tag(set_to_time):
    return str(set_to_time-datetime.now(timezone.utc))
