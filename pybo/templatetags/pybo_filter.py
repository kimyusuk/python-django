from django import template

register = template.Library()
@register.filter()
def sub(x,y):
    return x-y

