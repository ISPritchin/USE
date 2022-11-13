from itertools import product

count = 0
for x in product("ШКОЛА", repeat=3):
    comb = "".join(x)
    count += comb.count('К') == 1

print(count)