from django.template import Library
register = Library()

@register.filter
def status_tags(status):
    if status == 'a' :
        return '学生'
    elif status == 'b':
        return '老师'
    else :
        return '管理员'

