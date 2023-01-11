from atexit import register
from django import template

register = template.Library()


@register.filter
def display_point(point_count):
    html=""
    for i in range(point_count):
        html+='<i class="fa fa-star active"></i>'
    for i in range(5-point_count):
        html+='<i class="fa fa-star"></i>'
    return html

@register.filter
def display_average(comments):
    total=0
    numberOfComments = len(comments)
    for comment in comments:
       total+=comment.point
    
    try:
        percentage=int(total/(numberOfComments*5)*100)
    except: 
        percentage=0
    return percentage