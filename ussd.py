print('''Welcome to UBA USSD banking
   Enter your pin
      ''')
user = input('4-digit PIN: ')

print('''\nWelcome to UBA USSD banking
      1. Airtime-Self
      2. Airtime-Others
      3. Trsf-UBA
      4. Trsf-Other Banks
      5. Trsf-Microfinance &others
      6. Trsf -UBA perpaid
      7. Check Balance
      8. Next
      ''')

user = int(input('Option: '))
if user == 8 :
    exit()
elif user == 1 :
    print('\nPlease enter amount(#50-#10,000)')
    user = input('Amount: ')
    print('\nYour transaction is being processed')

elif user == 2 :
    print('\nPlease enter beneficiary phone number: ')
    user = input('Phone number: ')
    print('\nPlease enter amount(#50-#10,000)')
    user = input('Amount: ')
    print('\nYour transaction is being processed')

elif user == 7 :
    print('''\nTransaction fee of #10 applies.
            Do you wish to continue
            1. Yes
            2. No
          ''')
    user = int(input('Option: '))
    if user == 1:
        print('\nYour account balance is #499,911.23')
    elif user == 2:
        exit()

elif user == 3 or 4 or 5 or 6 :
    print('\nPlease enter beneficiary account number/name: ')
    user = input('Account number/name: ')
    print('''Bank:
          1. Access Bank
          2. Polaris Bank
          3. Guaranty Trust Bank
          4. First Bank
          5. Others
    ''')
    response = int(input('Option: '))
    if response == 1 or 2 or 3 or 4: 
        print('\nPlease enter amount(#50-#100,000)')
        user = input('Amount: ')
        print('\nYour transaction is being processed') 
    
else: exit() 
        





