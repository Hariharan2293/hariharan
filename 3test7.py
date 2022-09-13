from itertools import permutations

p= list((input("how many number u want to add:")))

comb = permutations(p, len(p))
for k in comb:
    print(k)