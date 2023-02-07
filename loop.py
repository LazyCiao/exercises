print('Printing current and previous number and their sum in a range(10)')

previous_num = 0

for i in range(1, 11):

    last_number = i - 1 
    sum_numbers = i + last_number

    print('current number', i, f'Previous Number', last_number, 'Sum: ', sum_numbers)