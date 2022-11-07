# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать значения от -1000 до 1000 включительно.
#
# Определите количество пар элементов последовательности, в которых хотя бы одно число кратно 5 или 7,
# а сумма чисел пары не превышает максимальное число последовательности, оканчивающиеся на две одинаковые цифры.

# В ответе запишите количество подходящих под условие пар, а затем максимальную из сумм чисел таких пар.
# В данной задаче под парой подразумевается два подряд идущих числа.
#
# Например, для чисел 22 5 15 21 -7 -10 ответом будет пара чисел 3 20.

a = [int(x) for x in open("17.txt")]

# максимальное число последовательности, оканчивающиеся на две одинаковые цифры.
m = -1000
for x in a:
    if x > m and x % 10 == x // 10 % 10:
        m = x

count = 0
max_s = 0
for i in range(1, len(a)):
    first = a[i - 1]
    second = a[i]
    s = first + second
    if s <= m and (first % 5 == 0 or first % 7 == 0 or second % 5 == 0 or second % 7 == 0):
        count += 1
        max_s = max(max_s, s)

print(count, max_s)