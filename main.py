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
    num = int(input('What number: '))
    str_c = input('Input String: ')
    valid = []
    test_str = []
    if num == 1:
        validity = string_checker1(str_c)
        print(validity)

    elif num == 2:
        validity = string_checker1(str_c)
        print(validity)



if __name__ == '__main__':
    main()

