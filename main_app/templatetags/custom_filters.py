# main_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='endswith')
def endswith(value, arg):
    """Checks if the value ends with the given argument"""
    return value.lower().endswith(arg.lower())
