from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('core/google_analytics.html', takes_context=True)
def google_analytics(context):
    context.update({
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID
    })
    return context
