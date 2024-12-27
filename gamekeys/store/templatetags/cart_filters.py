from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """
    Умножает два числа.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
