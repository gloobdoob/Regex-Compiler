#( aa + bb ) ( a + b )* ( a + b + ab + ba ) ( a + b + ab + ba )* ( aa + bab )* ( a + b + aa ) ( a + b + bb + aa )*

def string_checker(s):
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



def main():
    s = input('Enter String: ')
    validity = string_checker(s)
    print(validity)




if __name__ == '__main__':
    main()

