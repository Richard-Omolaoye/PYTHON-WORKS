class Bank:
    def __init__(self):
        self.bank_name = 'UBA Abuja'
        self.rc_no = '2033356'

        self.home()

    def home(self):
        user = int(input(f'''
                Welcome to {self.bank_name} {self.rc_no}
            1. Sign Up
            2. Sign In
        Option: '''))

        if user ==1:
            self.sign_up()
        elif user == 2:
            self.sign_in()
        else:
            exit()

    def sign_up(self):
        user = input('''
            You are signing up with your account in Nigeria
        Sign up using:
              1. Debit Card
              2. Prepaid Card
              3. Activate with *919# pin
              4. Account + Secure Pass
        Option: ''')

        if user == '1':
            self.Debit_card()
        elif user == '2':
            self.Prepaid_card()
        elif user == '3':
            self.Activate_919()
        elif user == '4':
            self.Secure_pass()
    
    def sign_in(self):
        user = input('Phone Number: ')
        user = input('Password: ')

    def Debit_card(self):
        print('MASTER CARD')
        user = int(input('Account Number: '))
        user = int(input('First Six Digits: '))
        user = int(input('Last Four Digits: '))
        user = int(input('Card Pin: '))
        user = int(input('Referral ID: '))

    
    def Prepaid_card(self):
        print('Sign Up')
        print('Please enter your mobile number that is registered with UBA and your birthdate')
        user = int(input('Phone Number: '))
        user = int(input('Birth Date: '))
        print('Please enter the last 4 digits of your UBA prepaid card')
        user = int(input('Card Number(Last 4 Digits): '))
        print('Enter your client identification number as specified on your prepaid card')
        user = int(input('Client Identification: '))
        user = int(input('Referral ID(Optional): '))

    
    def Activate_919(self):
        print('Sign Up')
        user = int(input('Phone Number: '))
        user = int(input('4 digit magic banking PIN: '))

    def Secure_pass(self):
        print('Sign Up')
        user = int(input('UBA Bank Account Number: '))
        user = int(input('Enter your Secure Pass code: '))
        user = int(input('Referral ID(optional): '))

UBA = Bank()

