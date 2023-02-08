number = input('Give me a number and I will tell you if that number is a palindrome: ')

pal = number[::-1]

if number == pal:
    print(f'The number {number} is a palindrome')
else:
    print(f'The number {number} is not a palindrome')