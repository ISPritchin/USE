# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописывается (дублируется) последняя цифра.
# 3) Затем справа дописывается бит чётности: 0, если
# в двоичном коде полученного числа чётное число единиц, и 1, если нечётное.
# 4) К полученному результату дописывается ещё один бит чётности.
#
# Укажите минимальное число R, большее 144, которое может быть получено
# в результате работы этого алгоритма.
# В ответе это число запишите в десятичной системе.

# Для последовательностей определен метод .count(x), который позволяет
# выполнять подсчёт элементов x в последовательности
# Например: a = [1, 5, 4, 4, 3, 1]
# a.count(4) -> 2
# a.count(3) -> 1
# number = "100110011"
# number.count('1') -> 5 (подсчёт количества единиц)

min_R = 1000
for N in range(1, 1000):
    number = bin(N)[2:]
    number = number + number[-1]
    # x = x + a -> x += a
    # number += number[-1] (подходит, только если дописываем в конец)
    for _ in range(2): # цикл, тело цикла (4 строки ниже) выполнятся дважды
        if number.count('1') % 2 == 0:
            number += '0'
        else:
            number += '1'

    R = int(number, 2)
    if 144 < R < min_R:
        min_R = R

print(min_R)
