from itertools import permutations

# 1 - Right
# 0 - Down
#n x n - Grid Size

bit_list = []
n = 20

for zero in range(n):
    bit_list.append('0')
for one in range(n):
    bit_list.append('1')

perms = []
perm_num = 0
for p in permutations(''.join(bit_list)):
    if ''.join(p) not in perms:
        perms.append(''.join(p))
        perm_num += 1

"""
perm_set = set(perms)

for perm in perm_set:
    print perm
"""
print perm_num
