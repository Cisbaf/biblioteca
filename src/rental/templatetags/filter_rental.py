from django import template

register = template.Library()

@register.filter(name="abs_value")
def abs_value(value):
    """Retorna o valor absoluto de um número."""
    try:
        return abs(value)
    except (ValueError, TypeError):
        return value
