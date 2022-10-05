# Автомат обрабатывает двузначное десятичное натуральное число N
# по следующему алгоритму.
#
# 1. Строится двоично-десятичное представление – каждый разряд
# десятичного числа кодируется с помощью 4 бит, затем полученные
# коды записываются друг за другом с сохранением незначащих нулей.
#
# 2. Полученная двоичная последовательность инвертируется –
# все нули меняются на единиц, все единицы на нули.
#
# 3. Полученное в результате этих операций двоичное число
# переводится в десятичную систему счисления.

def get_inv_number(number):
    inv_number = ""
    for digit in number:
        if digit == '1':
            inv_number += '0'
        else:
            inv_number += '1'
    return inv_number


for N in range(10, 100):
    number = str(N)

    bin_number = ""
    for digit in number:
        digit = bin(int(digit))[2:]
        bin_number = bin_number + (4 - len(digit)) * '0' + digit

    inv_number = get_inv_number(bin_number)
    R = int(inv_number, 2)
    if R == 151:
        print(N)
        break
