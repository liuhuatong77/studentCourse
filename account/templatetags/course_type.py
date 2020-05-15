from django.template import Library
register = Library()

@register.filter
def course_type(status):
    if status == 'a':
        return '必修'
    else:
        return '选修'