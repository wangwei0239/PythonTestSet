# coding=utf-8

def arabic_to_chinese(digit):
    digit = str(digit)
    simple_digit = u''
    for d in digit:
        simple_digit += NUM_CN.get(d)

    complex_digit = u''
    digit_len = len(digit)
    for index in range(digit_len):
        unit = digit_len - index
        partial_result = u''
        num = int(digit[index])
        if num != 0:
            if len(complex_digit) == 0 and get_unit(unit) == u'十':
                partial_result = get_unit(unit)
            else:
                partial_result = (NUM_CN.get(digit[index]) + get_unit(unit))
        elif is_all_zero(digit[index:]):
            origin_unit = unit
            unit -= (unit % 4 - 1)
            if origin_unit % 4 != 0 and origin_unit / 4 > 0:
                partial_result += get_unit(unit)
            complex_digit += partial_result
            break
        elif complex_digit[len(complex_digit)-1] != NUM_CN.get(u'0'):
            if is_all_zero_to_wan(digit, index):
                if unit % 4 - 1 == 0:
                    partial_result = get_unit(unit)
            else:
                partial_result = NUM_CN.get(digit[index])

        complex_digit += partial_result
    print complex_digit


def is_all_zero(num):
    return int(num) == 0


def is_all_zero_to_wan(num, index):
    lens = len(num) - index
    n = lens % 4
    value = num[index:index+n]
    if value == u'':
        value = u'1'
    return int(value) == 0


def get_unit(place):
    place -= 1
    small_unit_place = place
    big_unit_place = place
    if small_unit_place >= 4:
        small_unit_place = small_unit_place % 4
    unit = NUM_UNIT.get(str(small_unit_place))
    times = big_unit_place / 4

    big_unit = u''

    if times % 2 > 0:
        big_unit += u'万'

    num_yi = times / 2
    for x in range(0, num_yi):
        big_unit += u'亿'

    final_result = unit
    if small_unit_place == 0:
        final_result += big_unit

    return final_result
    # print unit


NUM_UNIT = {
    u'0': u'',
    u'1': u'十',
    u'2': u'百',
    u'3': u'千'
}

NUM_CN = {
    u'0': u'零',
    u'1': u'一',
    u'2': u'二',
    u'3': u'三',
    u'4': u'四',
    u'5': u'五',
    u'6': u'六',
    u'7': u'七',
    u'8': u'八',
    u'9': u'九'
}

if __name__ == '__main__':
    arabic_to_chinese(10000000)
