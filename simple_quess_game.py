import random

computer_number = random.randint(1, 10)

win = 0

while win != 1:
    input_value = int(input('Imput your guss: '))
    if input_value == computer_number:
        print('Congratulations! You have win the prize! Your guess is correct!!!')
        win = 1
    elif input_value < computer_number:
        print('Try again! Your number less then computer guss...')
    elif input_value > computer_number:
        print('Try again... this time your number is greater...')
    else:
        print('You have to enter number...')
