# 1. В шестеричной записи числа N дублируется последняя цифра
# 2. Получившееся число переводится в двоичное представление.
# 3. В получившейся записи дублируется последняя цифра.
# 4. Полученное в результате этих операций число переводится
# в десятичную систему счисления.

# Укажите максимальное число, меньшее 344, которое может являться
# результатом выполнения алгоритма.

def to_base(x, base):
    res = ""
    while x != 0:
        digit = x % base
        res = str(digit) + res
        x //= base             # // -> целочисленное деление 15 // 4 -> 3
    return res

print(to_base(42, 10))