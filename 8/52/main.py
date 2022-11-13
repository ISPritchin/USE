from itertools import product

count = 0
for x in product("ГАФНИЙ", repeat=4):
    comb = "".join(x)
    count += comb[0] != 'Й' and ('А' in x or 'О' in x)

print(count)