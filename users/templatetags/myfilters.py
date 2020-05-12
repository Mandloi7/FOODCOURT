from django import template

register = template.Library()

@register.filter(name='addcss')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

    	