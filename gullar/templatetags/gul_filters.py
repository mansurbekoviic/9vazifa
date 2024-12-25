from django import template

register = template.Library()

@register.filter
def tur_nomi(gul):
    return gul.tur.nom
