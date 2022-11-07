# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от -10000 до 10000 включительно.

# Определите и запишите в ответе сначала количество пар элементов последовательности,
# в которых сумма элементов не менее 100 и хотя бы одно число в паре отрицательное,
# затем максимальное из произведений элементов таких пар.

# В данной задаче под парой подразумевается два подряд идущих элемента последовательности.

a = [int(x) for x in open("17.txt")]

count = 0
max_p = float("-inf")
for i in range(1, len(a)):
    first = a[i - 1]
    second = a[i]
    s = first + second
    if s >= 100 and (first < 0 or second < 0):
        count += 1
        max_p = max(max_p, first * second)

print(count, max_p)
