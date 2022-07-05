#( aa + bb ) ( a + b )* ( a + b + ab + ba ) ( a + b + ab + ba )* ( aa + bab )* ( a + b + aa ) ( a + b + bb + aa )*
import exrex
import random
import re

def string_checker1(s):
    count = 0
    if s[:2] == 'aa' or s[:2] == 'bb':
        count = count + 1

    if s[-2:] == 'aa':
        count = count + 1
        if any(x in s[2:-2] for x in ['a', 'b', 'a', 'ba']):
            count = count + 1
        elif s[:2] + s[-2:] == s:
            count = count + 1

    elif s[-1] == 'a' or s[-1] == 'b':
        count = count + 1
        if any(x in s[2:-1] for x in ['a', 'b', 'a', 'ba']):
            count = count + 1

    if count == 3:
        return 'valid'
    else:
        return 'not valid'

#( ( 101 + ( 111 )* + 100 ) + ( 1 + 0 + 11 )* ) ( 1 + 0 + 01 )* ( 111 + 000 + 101 ) ( 1 + 0 )*

#( ( 101 + ( 111 )* + 100 ) + ( 1 + 0 + 11 )* )   ( 111 + 000 + 101 )
def string_checker2(s):
    if any(x in s for x in ['111', '000', '101']):
        return 'valid'
    else:
        return 'not valid'
    # if s[:3] == '101' or s[:3] == '100' or s[:3] == '111':
    #     count = count + 1
    #     if any(x in s[3:] for x in ['111', '000', ' 101']):
    #         count = count + 1
    #
    #
    # elif s[:2] == '11':
    #     count = count + 1
    #     if any(x in s[2:] for x in ['111', '000', ' 101']):
    #         count = count + 1
    #
    # elif s[0] == '0' or s[0] == '1':
    #     count = count + 1
    #     if any(x in s[1:] for x in ['111', '000', ' 101']):
    #         count = count + 1




    # if s[-3:] == '111' or s[-3:] == '000' or s[-3:] == '101':
    #     count = count + 1
    # elif len(s) > 3:
    #     if s[-1] == '1' or s[-1] == '0':
    #         count = count + 1

    #
    # if count == 2:
    #     return 'valid'
    # else:
    #     return 'not valid'

def pyregtest(reg, strr):
    pattern = re.compile(reg)
    if pattern.match(strr):
        return 'valid'
    else:
        return 'not valid'



def random_string(length, letters):
    return ''.join(random.choice(letters) for i in range(length))

def main():
    num = int(input('What number: '))
    n_test = int(input('how many to generate: '))
    max_length = int(input('how many characters: '))
    pyvalid = []
    valid = []
    test_str = []
    if num == 1:
        for i in range(n_test):
            #l1 = exrex.getone('(aa|bb)(a|b)*(a|b|ab|ba)(a|b|ab|ba)*(aa|bab)*(a|b|aa)(a|b|bb|aa)*')
            # ( aa + bb ) ( a + b )* ( a + b + ab + ba ) ( a + b + ab + ba )* ( aa + bab )* ( a + b + aa ) ( a + b + bb + aa )*
            l1 = random_string((random.randint(1, max_length)), 'ab')
            if l1 in test_str:
                l1 = random_string((random.randint(1, max_length)), 'ab')

            val = pyregtest('(aa|bb)(a|b)*(a|b|ab|ba)(a|b|ab|ba)*(aa|bab)*(a|b|aa)(a|b|bb|aa)*', l1)

            test_str.append(l1)
            validity = string_checker1(l1)
            valid.append(validity)
            pyvalid.append(val)

    elif num == 2:
        for i in range(n_test):
            #l2 = exrex.getone('((101|(111)*|100)|(1|0|11)*)(1|0|01)*(111|000|101)(1|0)*')
            #( ( 101 + ( 111 )* + 100 ) + ( 1 + 0 + 11 )* ) ( 1 + 0 + 01 )* ( 111 + 000 + 101 ) ( 1 + 0 )*
            l2 = random_string((random.randint(1, max_length)), '10')
            if l2 in test_str:
                l2 = random_string((random.randint(1, max_length)), '10')

            val = pyregtest('((101|(111)*|100)|(1|0|11)*)(1|0|01)*(111|000|101)(1|0)*', l2)
            test_str.append(l2)
            validity = string_checker2(l2)
            valid.append(validity)
            pyvalid.append(val)

    c = valid.count('not valid')
    pc = pyvalid.count('not valid')
    if valid == pyvalid:
        print('this works')
        print(f'ours:{c}/python:{pc}')
    else:
        print('this doesnt work')
        print(f'ours:{c}/python:{pc}')
        invp = [t for t, v, pv in zip(test_str, valid, pyvalid) if v == 'valid' and pv == 'not valid']
        inv = [t for t, v, pv in zip(test_str, valid, pyvalid) if v == 'not valid' and pv == 'valid']

        if len(invp) > 0:
            print('strings not valid in python re but valid in ours')
            print(invp)

        if len(inv) > 0:
            print('strings valid in python re but not valid in ours')
            print(inv)

    # if 'not valid' in valid:
    #     print('sucks')
    #     print(valid.count('not valid'), '/', n_test)
    #
    #     inv = [t for t, v in zip(test_str, valid) if v == 'not valid']
    #
    #     print(inv)
    # elif 'valid' in valid:
    #     print('nice')


main()

