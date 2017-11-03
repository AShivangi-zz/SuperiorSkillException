from django import template
register = template.Library()

def makefalse(value):
    value = False
    return value

def maketrue(value):
    value = True
    return value

register.filter('makefalse', makefalse)
register.filter('maketrue', maketrue)

