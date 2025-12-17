from django import template
from django.utils import timezone
from datetime import datetime

register = template.Library()

@register.filter
def model_type(instance):
    return type(instance).__name__

@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username

@register.filter
def get_posted_at_display(posted_at):
    delta = timezone.now() - posted_at
    minute = delta.total_seconds() / 60
    if minute < 60:
        message = f"Posté il y a {minute} minutes"
    elif minute < 1440:
        message = f"Posté il y a {round(minute/60)} heures"
    else:
        date_display = posted_at.strftime("%H:%M %d %m %y")
        message = f"Posté à {date_display}"
    return message