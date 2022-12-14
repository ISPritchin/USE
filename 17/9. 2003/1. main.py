# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно.
#
# Рассматривается множество элементов последовательности,
# которые делятся на 3 и не делятся на 7, 17, 19, 27.
#
# Найдите количество таких чисел и максимальное из них.

count = 0
max_x = float("-inf")
for x in open("17.txt"):
    x = int(x)
    if x % 3 == 0 and x % 7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 != 0:
        count += 1
        max_x = max(max_x, x)

print(count, max_x)