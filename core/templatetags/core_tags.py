

from django import template
from django.db.models import Avg
from django.utils.text import wrap

from numpy import number

register = template.Library()


@register.filter(name="split")
def get_code(number):
    # return str(number).split(' '.join(wrap(str(number), 4)))
    return str(number).join(wrap(str(number), 4))


@register.filter(name="class_color")
def get_color(value):
    if  value == "Active":
        return "text-success"
    if  value == "Inactive":
        return "text-info"
    if value == "Overdue":
        return "text-danger"



