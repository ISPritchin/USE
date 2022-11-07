# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно.

# Рассматривается множество элементов последовательности, больших 100, которые удовлетворяют следующим условиям:
# − цифра в разряде десятков не превышает 4;
# − цифра в разряде сотен принадлежит отрезку [3; 7].

# Найдите количество таких чисел и минимальное из них.

count = 0
min_x = float("inf")
for row in open("17.txt"):
    x = int(row)
    cond1 = x > 100
    cond2 = x // 10 % 10 <= 4
    cond3 = 3 <= x // 100 % 10 <= 7
    if cond1 and cond2 and cond3:
        count += 1
        min_x = min(min_x, x)

print(count, min_x)
