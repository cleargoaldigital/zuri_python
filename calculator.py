#initialize the number variables that accept inputs from users

firt_number = int(input('Enter first number: ')) #Accept only integers
second_number = int(input('Enter second number: ')) #Accept only integers

#the sum of the two numbers variable
add = firt_number + second_number
subtract = firt_number - second_number
divide = firt_number / second_number
multiply = firt_number * second_number
modulus = firt_number % second_number

#selection of choice of operator

selected_operator = input('Enter an operator, + = addition, - = subtraction, / = division, * = multiplication and % = remainder: ')
#result output based on selected operators

if selected_operator == '+':
   print('The addition of {0} and {1} is equal to {2}'.format(firt_number, second_number, add))

if selected_operator == '-':
   print('The subtraction of {1} from {0} is equal to {2}'.format(firt_number, second_number, subtract))

if selected_operator == '*':
   print('The multiplication of {0} and {1} is equal to {2}'.format(firt_number, second_number, multiply))

if selected_operator == '/':
   print('The division of {0} by {1} is equal to {2}'.format(firt_number, second_number, divide))
 
if selected_operator == '%':
   print('The remainder of the division of {0} by {1} is equal to {2}'.format(firt_number,second_number, modulus))
