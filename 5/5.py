# 1) Строится двоичная запись числа N.
# К этой записи дописываются справа ещё два разряда по следующему
# правилу:
#
# 2) Если число чётное, в конец числа (справа) дописывается 1,
# в противном случае справа дописывается 0.
#
# 3) Предыдущий пункт повторяется для записи с добавленной цифрой.
# Например, двоичная запись 1001 числа 9 будет
# преобразована в 100101.
#
# Полученная таким образом запись
# (в ней на два разряда больше, чем в записи исходного числа N)
# является двоичной записью числа – результата работы данного
# алгоритма.

# Укажите максимальное число N,
# для которого результат работы алгоритма будет меньше 171.
# В ответе это число запишите в десятичной системе счисления.

# x = x + a -> x += a

for N in range(1000, 1, -1):
    number = bin(N)[2:]

    for _ in range(2):
        if number[-1] == '0': # взять 1 элемент последовательности с конца
            number += '1'
        else:
            number += '0'

    R = int(number, 2)
    if R < 171:
        print(N)
        break