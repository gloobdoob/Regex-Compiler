import exrex
import random

def random_string(length, letters):
    return ''.join(random.choice(letters) for i in range(length))


reg1 = []
for s in range(500):
    l1 = exrex.getone('(aa|bb)(a|b)*(a|b|ab|ba)(a|b|ab|ba)*(aa|bab)*(a|b|aa)(a|b|bb|aa)')
    reg1.append(l1)


l2 = exrex.getone('((101|(111)*|100)|(1|0|11)*)(1|0|01)*(111|000|101)(1|0)*')

rand_str = []
max_length = 100
for i in range(1):
    str = random_string((random.randint(1, max_length)), 'ab')
    print(str)




