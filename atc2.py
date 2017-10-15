# coding=utf-8
UNIT_INTERVAL = 4
UNIT_GE = u''
UNIT_TEN = u'十'
UNIT_HUNDRED = u'百'
UNIT_THOUSAND = u'千'
UNIT_WAN = u'万'
UNIT_YI = u'亿'

NUM_UNIT = {
    u'0': UNIT_GE,
    u'1': UNIT_TEN,
    u'2': UNIT_HUNDRED,
    u'3': UNIT_THOUSAND
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


def arabic_to_chinese(digit):
    digit = str(digit)
    simple_digit = u''
    for d in digit:
        simple_digit += NUM_CN.get(d)

    complex_digit = u''
    digit_len = len(digit)
    for index in range(digit_len):
        # place is the index of digit from right to left, the index is start from 1
        place = digit_len - index
        partial_result = u''
        cur_digit = int(digit[index])
        if cur_digit != 0:
            if is_this_first_ten(complex_digit, place):
                # this is the first digit and it is ten, so just use unit instead of digit plus unit
                partial_result = get_unit(place)
            else:
                partial_result = (NUM_CN.get(digit[index]) + get_unit(place))
        elif is_all_zero(digit, index):
            origin_place = place
            # firstly use place reduce useless 0, then plus one for get the unit of the all 0.
            # like 0000, we need to put 1 before, then 10000 can get the big unit like wan and yi.
            place = place - place % 4 + 1
            # to check if current 0 is already after big unit, and if it is big than wan,
            # otherwise add wan and yi is unnecessary.
            if origin_place % 4 != 0 and origin_place / 4 > 0:
                partial_result += get_unit(place)
            complex_digit += partial_result
            break
        elif is_previous_digit_is_zero(complex_digit):
            if is_all_zero_to_wan(digit, index):
                if (place - place % 4 + 1) == 0:
                    partial_result = get_unit(place)
            else:
                partial_result = NUM_CN.get(digit[index])
        complex_digit += partial_result
    print complex_digit
    return [simple_digit, complex_digit]


def get_unit(place):
    # the place reduce 1, so the place will start from 0
    place -= 1
    # for unit like 千百十
    small_unit_place = place
    # for unit like 万，亿，万亿
    big_unit_place = place
    if small_unit_place >= UNIT_INTERVAL:
        small_unit_place = small_unit_place % UNIT_INTERVAL
    small_unit = NUM_UNIT.get(str(small_unit_place))
    big_unit_place_times = big_unit_place / UNIT_INTERVAL
    big_unit = u''
    if big_unit_place_times % 2 > 0:
        big_unit += UNIT_WAN
    num_yi = big_unit_place_times / 2
    for x in range(num_yi):
        big_unit += UNIT_YI
    final_unit = small_unit
    if small_unit_place == 0:
        final_unit += big_unit
    return final_unit


def is_this_first_ten(cur_complex_digit, place):
    return len(cur_complex_digit) == 0 and get_unit(place) == u'十'


def is_previous_digit_is_zero(cur_complex_digit):
    return cur_complex_digit[len(cur_complex_digit)-1] != NUM_CN.get(u'0')


def is_all_zero(num, index):
    return int(num[index:]) == 0


def is_all_zero_to_wan(num, index):
    rest_digit_num = len(num) - index
    mod_result = rest_digit_num % UNIT_INTERVAL
    value = num[index:index + mod_result]
    if value == u'':
        return False
    return int(value) == 0


if __name__ == '__main__':
    # is_all_zero_to_wan('10000', 0)
    arabic_to_chinese(10111)
