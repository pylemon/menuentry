# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_POST
from validator.utils import format_data, format_error


def validate_menu_entry_data(request):
    """

    :param request:
    :return:
    """
    return render_to_response('validator/validate_menu_entry_data.html', RequestContext(request))


@csrf_exempt
@require_POST
def format_input(request):
    """
    格式化输入， 返回渲染后的内容。

    :param request:
    :return:
    """
    data = request.POST.get('data', '')
    formatted_data, error = format_data(data)
    errors = format_error(error)
    ret = json.dumps({
        'formatted_data': formatted_data,
        'errors': errors,
    })
    return HttpResponse(ret, content_type='application/json')
