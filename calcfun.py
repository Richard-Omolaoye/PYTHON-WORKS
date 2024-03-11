class Calculator:
    def __init__(self) :
        self.alata = 'Alata Calculator'

        self.home()

    def home(self):
        user = input('''
                My Alata Calculator
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Modulus
            6. Floor Division
            7. Exponential
        Option: ''')

        if user =='1':
            self.add()
        elif user == '2':
            self.sub()
        elif user == '3':
            self.mul()
        elif user == '4':
            self.div()
        elif user == '5':
            self.mod()
        elif user == '6':
            self.flodiv()
        elif user == '7':
            self.exp()
    

    def add(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value + second_value
        print(f'Answer: {result}')
        self.home()

    def sub(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value - second_value
        print(f'Answer: {result}')
        self.home()

    def mul(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value * second_value
        print(f'Answer: {result}')
        self.home()

    def div(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value / second_value
        print(f'Answer: {result}')
        self.home()

    def mod(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value % second_value
        print(f'Answer: {result}')
        self.home()

    def flodiv(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value // second_value
        print(f'Answer: {result}')
        self.home()

    def exp(self):
        first_value = int(input('First Value: '))
        second_value = int(input('Second Value: '))
        result = first_value ** second_value
        print(f'Answer: {result}')
        self.home()

Alata = Calculator()