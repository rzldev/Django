from django import template

register = template.library()


@register.filter(name="cut")
def cut(value, arg):
    """
        This cuts out all valus of "arg" from the string!
    """
    return value.replace(arg, '')


# register.filter('cut', cut)
