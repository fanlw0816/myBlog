from django import template
from django.utils.safestring import mark_safe

register=template.Library()


@register.filter(name='plus')
def plus(value):
    return value + 1


@register.filter(name='subtract')
def subtract(value):
    return value - 1