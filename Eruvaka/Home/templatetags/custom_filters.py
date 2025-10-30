from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary by key"""
    if dictionary is None:
        return None
    return dictionary.get(key)

@register.filter
def calculate_savings(old_price, current_price):
    """Calculate savings between old price and current price"""
    if not old_price or not current_price:
        return 0
    try:
        old = Decimal(str(old_price))
        current = Decimal(str(current_price))
        if old > current:
            return old - current
    except (ValueError, TypeError):
        pass
    return 0

@register.filter
def calculate_discount_percentage(old_price, current_price):
    """Calculate discount percentage"""
    if not old_price or not current_price:
        return 0
    try:
        old = Decimal(str(old_price))
        current = Decimal(str(current_price))
        if old > current:
            return int(((old - current) / old) * 100)
    except (ValueError, TypeError, ZeroDivisionError):
        pass
    return 0

@register.filter
def format_price(value):
    """Format price with 2 decimal places"""
    try:
        return "{:.2f}".format(float(value))
    except (ValueError, TypeError):
        return "0.00"

@register.filter
def multiply(value, arg):
    """Multiply value by arg"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

