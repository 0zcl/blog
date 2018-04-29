from ..models import Post
from django import template
from ..models import Post, Category

# 为了能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数，
# 必须按照 Django 的规定注册这个函数为模板标签
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    # 获取数据库中前 num 篇文章
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    # 现按月归档的目的
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()

