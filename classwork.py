"""PRINTING MY NAME 100 TIMES"""

for count in range(101):
    print(f'{count} - ENIMAKPOKPO EHIABHI EHIS')


'''PRINTING INTEGERS AND THEIR SQUARES FROM 1 TO 20'''

for num in range(21):
    num_square = num*num
    print(f'{num} --- {num_square}')


'''PRINTING A RECTANGLE SHAPE'''

number = [15, 2, 2, 15]
for count in number:
    if count == 15:
        print(f' *' * count)
    else:
        print(f' *' + f'                           ' + f'*')


'''PRINTING A RIGHT-TRIANGLE SHAPE'''

number = [1, 2, 3, 4, 5, 6]
for count in number:
    print(f' *' * count)


'''PRINTING AN 'A' SHAPE'''

for ro in range(4):
    if ro == 0:
        print(f'    ' + f'*' + f'   ')
    elif ro == 1:
        print(f'   ' + f'*' + f' ' + f'*' + f'  ')
    elif ro == 2:
        print(f'  ' + f'*' + f' ' +f'*' + f' ' + f'*' + f'  ')
    else:
        print(f' ' + f'*' +f'     ' + f'*' + f' ')


'''CALCULATING AN f(n) = 3^(n!) FUNCTION'''


def factorial(n):
    if n == 1:
        return 1
    else:
        s = n * factorial(n-1)
        return s
        
        
n = int(input("Please enter an integer: "))
k = factorial(n)
i = 0
result = 1
while i < k:
    result = result * 3
    i += 1
print(f'f({k})= {result}')


'''CALCULATING THE FACTORIAL OF A NUMBER'''


def factorial(n):
    if n == 1 or n == 0:
        print(f'{n} factorial is 1')
        return 1
    else:
        s = n * factorial(n - 1)
        print(f'{n} factorial is {s}')
        return s


n = int(input("Please enter an interger: "))
factorial(n)
