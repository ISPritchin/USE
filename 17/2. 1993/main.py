# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# сумма которых кратна 3 и не кратна 6, а произведение оканчивается на 8,
# затем максимальную из сумм элементов таких пар.
#
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

a = [int(x) for x in open("17.txt")]

n_pairs = 0
max_sum = -100000
for i in range(1, len(a)):
    first = a[i - 1]
    second = a[i]
    s = first + second
    p = first * second
    if s % 3 == 0 and s % 6 != 0 and abs(p) % 10 == 8:
        n_pairs += 1
        max_sum = max(max_sum, s)

print(n_pairs, max_sum)