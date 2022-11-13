from itertools import product

count = 0
for x in product("ЛЕТО", repeat=4):
    comb = "".join(x)
    count += comb[0] in "ЛТ"

print(count)