from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
@register.filter('LowerCase')
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()
#register.filter('LowerCase',lower)