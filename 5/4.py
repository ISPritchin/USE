# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются разряды по следующему правилу:
# а) если единиц больше, чем нулей, в конец дописывается 0,
# б) иначе в начало строки дописывается две 1.
# 3) Повторяется пункт 2

# Укажите минимальное число N, при вводе которого получится
# значение R больше, чем 500.
# В ответе полученное число запишите в десятичной системе.

for N in range(1, 1000):
    number = bin(N)[2:]

    for _ in range(2):
        if number.count('1') > number.count('0'):
            number = number + '0'
        else:
            number = "11" + number

    R = int(number, 2)
    if R > 500:
        print(N)
        break