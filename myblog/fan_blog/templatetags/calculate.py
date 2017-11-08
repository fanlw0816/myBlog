from django import template
from django.utils.safestring import mark_safe

register=template.Library()


@register.filter(name='plus')
def plus(value):
    return value + 1


@register.filter(name='subtract')
def subtract(value):
    return value - 1


@register.filter(name='slice')
def slice(number):
    return list(range(number-2, number+3))


@register.filter(name='slice1')
def slice1(number):
    return list(range(1, 6))


@register.filter(name='slice2')
def slice2(number):
    return list(range(number-4, number+1))
