import datetime

from django import template
from django.db.models import Avg
from textwrap import wrap



from core.models import Card

register = template.Library()


@register.filter(name="split")
def get_code(number):
    return ' '.join(wrap(str(number), 4))


@register.filter(name="class_color")
def get_color(value):
    if  value == "Active":
        return "text-success"
    if  value == "Inactive":
        return "text-danger"
    if value == "Overdue":
        return "text-warning"

@register.filter(name="datesplit")
def get_code(value):
    return value.strftime("%d/%m/%Y")\





