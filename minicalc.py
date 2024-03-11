print('''
        MY SIMPLE ALATA CALCULATOR
      1. Addition
      2. Subtraction
      3. Division
      4. Multiplication
      5. Exit
''')

user = float(input('Option: '))
if user == 5:
    exit()
else:
    firstvalue = float(input('\nFirst Value: '))
    secondvalue = float(input('Second Value: '))

    if user == 1 :
        Answer = firstvalue + secondvalue
        print(f'\nAnswer: {Answer}')

    elif user == 2 :
        Answer = firstvalue - secondvalue
        print(f'\nAnswer: {Answer}')

    elif user == 3 :
        Answer = firstvalue/secondvalue
        print(f'\nAnswer: {Answer}')

    elif user == 4 :
        Answer = firstvalue*secondvalue
        print(f'\nAnswer: {Answer}')





