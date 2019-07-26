from django.template import Library

register = Library()


@register.filter(name='active')
def active(value, arg):
    if int(value) == int(arg):
        return 'active-page'
    return None
