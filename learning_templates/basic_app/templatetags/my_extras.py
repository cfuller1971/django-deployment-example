from django import template

register = template.Library()

# Use a decorator to register a custom filter
@register.filter(name='cunt')
def cunt(value, arg):
    '''
    This cuts out all values of "arg" from the string!!!
    '''

    return value.replace(arg, '')

# register.filter('cunt', cunt)
