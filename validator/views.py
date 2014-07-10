# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from validator.utils import format_data, format_error


def validate_menu_entry_data(request):
    """

    :param request:
    :return:
    """
    context = RequestContext(request)
    data = request.GET.get('data', '')
    formatted_data, error = format_data(data)
    errors = format_error(error)
    context.update({
        'data': data,
        'formatted_data': formatted_data,
        'errors': errors,
    })
    return render_to_response('validator/validate_menu_entry_data.html', context)
