#( aa + bb ) ( a + b )* ( a + b + ab + ba ) ( a + b + ab + ba )* ( aa + bab )* ( a + b + aa ) ( a + b + bb + aa )*
import exrex
import random

def string_checker1(s):
    count = 0
    if s[:2] == 'aa' or s[:2] == 'bb':
        count = count + 1

    elif s[-2:] == 'aa':
        count = count + 1
        if any(x in s[2:-2] for x in ['a', 'b', 'a', 'ba']):
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
    count = 0
    if s[:3] == '101' or s[:3] == '100' or s[:3] == '111' or s[0] == '1' or s[0] == '0' or s[:2] == '11':
        count = count + 1

    if s[-3:] == '111' or s[-3:] == '000' or s[-3:] == '101' or s[-1] == '1' or s[-1] == '0':
        count = count + 1

    if count == 2:
        return 'valid'
    else:
        return 'not valid'

def random_string(length, letters):
    return ''.join(random.choice(letters) for i in range(length))

def main():
    num = input('What number: ')
    n_test = int(input('how many to generate: '))
    max_length = 100
    print('hi')
    if num == 1:
        valid = []
        for i in range(n_test):
            #l1 = exrex.getone('(aa|bb)(a|b)*(a|b|ab|ba)(a|b|ab|ba)*(aa|bab)*(a|b|aa)(a|b|bb|aa)')
            #l1 = random_string((random.randint(1, max_length)), 'ab')
            print(l1)
            validity = string_checker1(l1)
            valid.append(l1)

        print(valid)
        if 'not valid' in valid:
            print('sucks')
        elif 'valid' in valid:
            print('nice')
    else:
        valid = []
        for i in range(n_test):
            strr = '( ( 101 + ( 111 )* + 100 ) + ( 1 + 0 + 11 )* ) ( 1 + 0 + 01 )* ( 111 + 000 + 101 ) ( 1 + 0 )*'
            strr = strr.replace(' ', '')
            strr = strr.replace('+', '|')
            l2 = exrex.getone(strr)
            validity = string_checker2(l2)
            valid.append(validity)

        print(valid)
        if 'not valid' in valid:
            print('sucks')
        elif 'valid' in valid:
            print('nice')




if __name__ == '__main__':
    main()

