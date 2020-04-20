from django.shortcuts import render, redirect

from apps.user.utils import get_all_navbar, en_get_all_navbar
from functools import wraps


def decorator_template(pagename=None):

    def decorator_view(func):
        wraps(func)

        def inner_func(self, request, *args, **kwargs):
            try:
                data = func(self, request, *args, **kwargs)
                if data.get('error'):
                    return redirect(data.get('render_url'))

                if data is None:
                    data = dict()
            except Exception as e:
                print(e)
                data = dict()

            context = get_all_navbar(context=data)

            return render(request, pagename, context)
        return inner_func

    return decorator_view


def en_decorator_template(pagename=None):

    def decorator_view(func):
        wraps(func)

        def inner_func(self, request, *args, **kwargs):
            try:
                data = func(self, request, *args, **kwargs)
                if data.get('error'):
                    return redirect(data.get('render_url'))

                if data is None:
                    data = dict()
            except Exception as e:
                data = dict()

            context = en_get_all_navbar(context=data)

            return render(request, pagename, context)
        return inner_func

    return decorator_view
