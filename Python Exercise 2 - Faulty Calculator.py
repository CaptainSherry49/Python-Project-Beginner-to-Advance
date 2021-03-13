# ----------------------------- Faulty Calculator ------------- #

# Wrong Answers = (45 * 3 = 555 ), (56 + 9 = 77), (56/6 = 4)

operators = ['+', '-', '*', '/']

print('These are the operators which is used in your Calculation: ')
print(operators)
val1 = int(input('Enter first value: '))
operator = input('Please Enter your Operator: ')
val2 = int(input('Enter Second value: '))

if val1 == 45 and operator == '*' and val2 == 3:
    print('Your Answer is  "555" ')
elif val1 == 56 and operator == '+' and val2 == 9:
    print('Your Answer is  "77" ')
elif val1 == 56 and operator == '/' and val2 == 6:
    print('Your Answer is "4" ')
elif operator == '*':
    print(f'Your Answer is {val1*val2}')
elif operator == '+':
    print(f'Your Answer is {val1+val2}')
elif operator == '-':
    print(f'Your Answer is {val1-val2}')
elif operator == '/':
    print(f'Your Answer is {val1/val2}')
else:
    print('Enter Valid Value !')