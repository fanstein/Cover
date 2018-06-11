from django import template

register = template.Library()


@register.filter()
def rep(value, arg):
    return value.replace(arg, ' ')


@register.filter()
def get_list(value, arg):
    return value.split(arg)