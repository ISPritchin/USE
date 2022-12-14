# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится троичная запись числа N
# 2. В конец записи (справа) дописывается остаток от деления числа N на 3.
# 3. Результат переводится из троичной системы в десятичную и
# выводится на экран.

# Пример. Дано число N=11. Алгоритм работает следующим образом:
# 1. Троичная запись числа N: 102
# 2. Остаток от деления 11 на 3 равен 2, новая запись 1022
# 3. На экран выводится число 35.

# Какое наименьшее трёхзначное число может появиться на экране в результате
# работы автомата?

# Продублировать последнюю цифру числа N в системе счисления S означает
# следующее:
# N = N * S + (N % S)

for N in range(1, 1000):
    R = N * 3 + N % 3
    if R >= 100:
        print(R)
        break
