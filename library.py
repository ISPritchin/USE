def to_base(x, base):
    res = ""
    while x != 0:
        digit = x % base
        res = str(digit) + res
        x //= base  # // -> целочисленное деление 15 // 4 -> 3
    return res


def invert_number(number):
    inv_number = ""
    for digit in number:
        if digit == '1':
            inv_number += '0'
        else:
            inv_number += '1'

    return inv_number