# Автомат обрабатывает двузначное десятичное натуральное число N
# по следующему алгоритму.
#
# 1. Строится двоично-десятичное представление – каждый разряд
# десятичного числа кодируется с помощью 4 бит, затем полученные
# коды записываются друг за другом с сохранением незначащих нулей.
# 23 -> 0010 0011

# 2. Полученная двоичная последовательность инвертируется –
# все нули меняются на единиц, все единицы на нули.
#
# 3. Полученное в результате этих операций двоичное число
# переводится в десятичную систему счисления.

# Укажите N после обработки которого результатом
# выполнения алгоритма будет число 151

def invert_number(number):
    inv_number = ""
    for digit in number:
        if digit == '1':
            inv_number += '0'
        else:
            inv_number += '1'

    return inv_number


for N in range(10, 100):
    v1 = N // 10
    v2 = N % 10

    number = bin(v1)[2:].zfill(4) + bin(v2)[2:].zfill(4)
    inv_number = invert_number(number)
    R = int(inv_number, 2)

    if R == 151:
        print(N)
        break