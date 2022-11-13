from itertools import product

count = 0
for x in product("ЕИЙКНОТ", repeat=7):
    comb = "".join(x)
    count += "КОТ" in comb

print(count)