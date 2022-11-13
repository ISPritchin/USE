from itertools import product

count = 0
for x in product("ТОК", repeat=6):
    comb = "".join(x)
    count += comb[0] in "ТК"

print(count)