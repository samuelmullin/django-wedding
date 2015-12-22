from django import template

register = template.Library()

@register.inclusion_tag('form_field.html')
def form_field(field):
    context = {'field': field,}
    return context
