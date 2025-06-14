from itertools import permutations

s = input().strip()

# generate all permutations
all_perms = set(permutations(s))  # set removes duplicates

# convert tuples to strings
perm_strings = sorted(''.join(p) for p in all_perms)

# output
print(len(perm_strings))
for p in perm_strings:
    print(p)
