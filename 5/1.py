# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.

# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда
# по следующему правилу:

# а) складываются все цифры двоичной записи числа N,
# и остаток от деления суммы на 2 дописывается в конец числа (справа).
# Например, запись 11100 преобразуется в запись 111001;

# б) над этой записью производятся те же действия – справа
# дописывается остаток от деления суммы её цифр на 2.
# Полученная таким образом запись
# (в ней на два разряда больше, чем в записи исходного числа N)
# является двоичной записью искомого числа R.
#
# Укажите такое наименьшее число N, для которого результат работы
# данного алгоритма больше числа 77.
# В ответе это число запишите в десятичной системе счисления.

# Последовательности: строки, списки, кортежи и др
# Над последовательностями определены срезы.
# a = [1, 2, 3, 4, 5]
# a[2:] -> [3, 4, 5]
# number = "0b1111010010"
# number[2:] -> "1111010010"

# Для последовательностей определен метод .count(x), который позволяет
# выполнять подсчёт элементов x в последовательности
# Например: a = [1, 5, 4, 4, 3, 1]
# a.count(4) -> 2
# a.count(3) -> 1
# number = "100110011"
# number.count('1') -> 5 (подсчёт количества единиц)

for N in range(1, 1000):
    number = bin(N)[2:]           # вернёт строку (!)

    for _ in range(2):            # цикл, действия в цикле выполнятся 2 раза
        s = number.count('1')
        number = number + str(s % 2)

    # int(number, 2) преобразует строку number в число
    # при условии, что число записано в 2-ой системе счисления
    R = int(number, 2)
    if R > 77:
        print(N)
        break
