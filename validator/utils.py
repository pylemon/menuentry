# -*- coding: utf-8 -*-
LINE_TYPES = {
    'empty': '空',
    'comment': '注释',
    'section_name': '菜品分类名称',
    'item_name': '菜品名称',
    'item_price': '菜品价格',
    'eof': '文件结束',
}

TYPE_PIPELINE = {
    'empty': LINE_TYPES.keys(),
    'comment': LINE_TYPES.keys(),
    'section_name': {'empty', 'comment', 'item_name'},
    'item_name': {'empty', 'comment', 'item_price'},
    'item_price': {'empty', 'comment', 'section_name', 'item_name', 'eof'},
    'eof': {}
}

def get_line_type(line):
    """
    获取一个行的类型的逻辑。

    :param line:
    :return:
    """
    line = line.strip()
    if line == '':
        return 'empty'

    try:
        float(line)
    except ValueError:
        pass
    else:
        return 'item_price'

    if line.startswith('#'):
        return 'comment'
    elif line.startswith('*'):
        return 'section_name'
    else:
        return 'item_name'


def format_error(error):
    """
    格式化错误信息。

    :param error:
    :return:
    """
    if not error:
        return []
    else:
        ret = []
        for idx, msg in sorted(error.items(), key=lambda x: x[0]):
            ret.append('第{}行错误，{}'.format(idx+1, msg))
        return ret


def check_price(price):
    """
    检查一个价格是否是合法的，如果不合法就返回对应的错误信息。

    :param price:
    :return:
    """
    try:
        price = float(price)
    except ValueError:
        return '价格错误'

    if not 0 <= price <= 9999:
        return '价格超出范围，价格的范围需要在0～9999之间。'


def format_data(data):
    """

    :param data:
    :return:
    """
    data_list = data.split('\n')

    # 截取带行号的数据信息，剔除掉空行与注释。
    non_empty_data = {
        idx: i for idx, i in enumerate(data_list)
        if get_line_type(i) not in ('empty', 'comment')
    }

    error_data = dict()
    first_item = True
    for i, (idx, data) in enumerate(non_empty_data.items()):
        line_type = get_line_type(data)

        # 检查第第一个元素的类型是否是一个 section_name
        if first_item:
            if line_type != 'section_name':
                error_msg = '第一项内容必须是一个 [{}]'.format(LINE_TYPES['section_name'])
                error_data[idx] = error_msg
            first_item = False

        # 检查菜品价格是否合法
        if line_type == 'item_price':
            error_msg = check_price(data)
            if error_msg:
                error_data[idx] = error_msg

        # 检查下一项内容是否是正确的类型
        try:
            next_line_type = get_line_type(non_empty_data.items()[i+1][1])
        except IndexError:
            next_line_type = 'eof'

        if next_line_type not in TYPE_PIPELINE[line_type]:
            error_msg = '下一项内容不能是 [{}]'.format(LINE_TYPES[next_line_type])
            error_data[idx] = error_msg

    # 获取带行号和错误标记的格式化数据
    ret = list()
    for index, data in enumerate(data_list):
        error = False
        if index in error_data:
            error = True

        ret.append(('{:0>3}'.format(index+1), data, error))

    return ret, error_data
