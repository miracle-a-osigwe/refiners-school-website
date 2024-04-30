from django import template
from mcq.models import Question


register = template.Library()

# @register.filter(is_safe=True)
@register.inclusion_tag('fieldset.html')
def add(question):
    new_question = Question
    return new_question


@register.simple_tag()
def locate(object, index):
    """
    Return the index position of an object.
    """
    return object[index]
