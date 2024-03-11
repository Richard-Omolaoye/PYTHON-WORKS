class ussd :
    def __init__(self):
        self.USSD_Name = 'UBA USSD'

        self.home()

    def home(self):
        user = input ('''Welcome to UBA USSD banking
            Enter your 4-digit pin: ''')
        
        option = int(input ('''
            1. Airtime-Self
            2. Airtime-Others
            3. Trsf-UBA
            4. Trsf-Other Banks
            5. Trsf-Microfinance &others
            6. Trsf -UBA perpaid
            7. Check Balance
            8. Next
        OPTION: '''))

        if option == 8 :
            exit()
            
        elif option == 1 :
            self.Airtime_self()

        elif option == 2 :
            self.Airtime_Others()

        elif option == 7 :
            self.Check_Balance()

        elif user == 3 or 4 or 5 or 6 :
            self.other_options()

        else:  
            exit() 

    def Airtime_self(self):
        user = input('Please enter amount(#50-#10,000): ')
        print('\nYour transaction is being processed')

    def Airtime_Others(self):
        user = input ('\nPlease enter beneficiary phone number: ')
        user = input ('\nPlease enter amount(#50-#10,000): ')
        print('\nYour transaction is being processed')

    def Check_Balance(Self):
        user = int(input ('''\nTransaction fee of #10 applies.
                    Do you wish to continue
                    1. Yes
                    2. No
                Option: '''))
        if user == 1:
            print('\nYour account balance is #499,911.23')
        elif user == 2:
            exit()
    
    def other_options(self):
        user = input ('\nPlease enter beneficiary account number/name: ')
        user = int(input ('''Bank:
                1. Access Bank
                2. Polaris Bank
                3. Guaranty Trust Bank
                4. First Bank
                5. Others
            Option: '''))
        if user == 1 or 2 or 3 or 4: 
            user = input ('\nPlease enter amount(#50-#100,000): ')
            print('\nYour transaction is being processed') 

UBA_USSD = ussd()