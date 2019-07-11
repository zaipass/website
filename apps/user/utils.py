from apps.user.models import NavBar

from apps.user.constants import position_type


def get_all_navbar(context=dict()):

    nav_list = NavBar.objects.filter(is_published=True).order_by('nav_num')

    context.update({'navbar': nav_list})

    return context


def get_next_news_not_position(news_obj):
    """ 下一篇文章防止是'招聘信息' """
    if news_obj:
        if news_obj.types.typename == position_type:
            news_obj = news_obj.get_next_by_create_time()
            return get_next_news_not_position(news_obj)
        else:
            return news_obj


def get_pre_news_not_position(news_obj):
    """ 上一篇文章防止是'招聘信息' """
    if news_obj:
        if news_obj.types.typename == position_type:
            news_obj = news_obj.get_previous_by_create_time()
            return get_pre_news_not_position(news_obj)
        else:
            return news_obj


def serializer_function(sf, objects, is_many=False):
    if is_many:
        serializer = sf.serializer_class(objects, many=is_many)
    else:
        serializer = sf.serializer_class(objects)

    return serializer.data
