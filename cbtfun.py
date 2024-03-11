class CBT:
    def __init__(self) -> None:
        self.Okoro_CBT = 'Okoro Foundation'

        self.home()

    def home(self):
        user = int(input('''Good day and trust you are doing fine
                This is the Okoro Foundation Scholarship Test
                Fill in the number of students taking the test and their names
                Number of Students: '''))
        nameofstudents = [input(f'Name of Students {x+1}: \n') for x in range (user)]
        print(f'Welcome {nameofstudents}')
        
        Question =  {
            '1. Who is the present president of Nigeria? A. Goodluck Jonathan B. Muhammadu Buhari C. Nnamdi Azikwe D. Bola Ahmed Tinubu' : 'D',
            '2. How many states are in Nigeria? A. 30 B. 32 C. 34 D. 36': 'D',
            '3. How many continents are in the world? A. 10 B. 6 C. 7 D. 8': 'C',
            '4. Who is the current president of the United States? A. Joe Biden B. Bill Clinton C. Barack obama D. Donald Trump': 'A',
            '5. Who is the first person to land on the moon? A. Joe Biden B. Isaac Newton C. Neil Armstrong D. Thomas Edinson': 'C',
            '6. How many ethnic groups do we have in Nigeria? A. 500 B. 250 C. 766 D. 520': 'C',
            '7. Democracy day is celebrated on? A. June 10 B. June 11 C. June 12 D. June 13': 'C',
            '8. What is the most populated country in the world? A. United State of America B. China C. India D. Russia': 'D',
            '9. The hottest region in the world is called? A. Sahel Desert B. Antantica Desert C. Indian Desert D. Sahara Desert':'D',
            '10. Who formed the first political party in Nigeria? A. Herbert Macaulay B. Obafemi Awolowo C. Nnamdi Azikwe D. MKO Abiola':'A'  }
            
        for key,value in Question:
            print(key)
        user=input('Option: ')
        if user == 'value':
            print('Correct')


take_test()