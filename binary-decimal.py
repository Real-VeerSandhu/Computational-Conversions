def binary_decimal(input):
    total = 0
    str_binary = str(input)[::-1]
    for i in range(len(str_binary)):
        total += 2**int(i) * int(str_binary[i])
    return total

def decimal_binary(input):
    if input >= 1:
        decimal_binary(input // 2)
    global x
    x.append(input % 2)
    return x

# Inputs

first = input('\nInput integer (I) or binary (B): ')

check = False
while check == False:
    if (first == 'I' or first == 'B'):
        check == True
        print('-'*50)
        break
    else:
        check == False
        print('\n*Invalid, enter again*\n')
        first = input('Input decimal (I) or binary (B): ')


# Find route
if first == 'B':
    binary = int(input('Enter binary value: '))
    print('Decimal/Integer value: ', end='')
    print(binary_decimal(binary))
else:
    integer = int(input('Enter integer value: '))
    print('Binary value: ', end='')
    x = []
    for i in (decimal_binary(integer)[1:]):
        print(i, end='')
    print('')
    


