from django import template
import markdown
from django.utils.safestring import mark_safe



register = template.Library()

@register.filter
def mark(x): #입력된 문자열을 html로 변환 시켜주는 것.
    #nl2br(줄바꿈 문자 -> <br>, fenced_code(마크다운))
    #nl2br 마크다운에서 줄바꿈은 스페이스 두번이다.
    extensions = ['nl2br', 'fenced_code']
    return mark_safe(markdown.markdown(x, extensions=extensions))

@register.filter
def sub(x,y):
    #@register.filter : 템플릿에서 필터로 사용할수 있게 된다. 빼기 필터.
    return x-y

