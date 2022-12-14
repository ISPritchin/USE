# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
#
# Определите и запишите в ответе сначала количество троек элементов последовательности,
# в которых числа расположены в порядке возрастания, затем минимальную из разностей
# наибольшего и наименьшего элементов таких троек.
#
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

a = [int(x) for x in open("17.txt")]

n3 = 0
min_diff = float("inf")
for i in range(2, len(a)):
    first = a[i - 2]
    second = a[i - 1]
    third = a[i]
    if first < second < third:
        n3 += 1
        min_diff = min(min_diff, max(first, second, third) - min(first, second, third))

print(n3, min_diff)
