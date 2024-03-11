
print('''Good day and trust you are doing fine
    This is the Okoro Foundation Scholarship Test
    Fill in the number of students taking the test and their names''')

number = int(input('Number of Students: '))

nameofstudents = [input(f'Name of Students {x+1}: \n') for x in range (number)]

scorelist=[]

for eachstudent in nameofstudents :
    print(eachstudent, 'welcome to the Okoro Foundation scholarship test, you have 5 minutes to answer the 10 questions and at the end of the test, your total score out of 100 will be displayed.')

    print('''
            Are you ready for the test?
        A. YES
        B. NO 

        ''')
    count = 0
    option = input('Option: ').strip().capitalize()

    if option == 'A' :
        print('''
            WELCOME

    #             1. Who is the present president of Nigeria?
    #         A. Goodluck Jonathan
    #         B. Muhammadu Buhari
    #         C. Nnamdi Azikwe
    #         D. Bola Ahmed Tinubu
    #     ''')
    elif option == 'B' :
        print('Thank you for your time!')
        exit()

    option = input('Answer: ').strip().capitalize()
        
    if option == 'D' :
        count += 10

    print('''
            2. How many states are in Nigeria?
            A. 30
            B. 32
            C. 34
            D. 36
        ''')

    option = input('Answer: ').strip().capitalize()

    if option =='D' :
        count += 10

    print('''
            3. How many continents are in the world?
            A. 10
            B. 6
            C. 7
            D. 8
        ''')

    option = input('Answer: ').strip().capitalize()

    if option == 'C' :
        count += 10
    print('''
            4. Who is the current president of the United States?
            A. Joe Biden
            B. Bill Clinton
            C. Barack obama
            D. Donald Trump
        ''')

    option = input('Answer: ').strip().capitalize()


    if option == 'A' :
        count += 10
    print('''
            5. Who is the first person to land on the moon?
            A. Joe Biden
            B. Isaac Newton
            C. Neil Armstrong
            D. Thomas Edinson
        ''')

    option = input('Answer: ').strip().capitalize()

    if option == 'C' :
        count += 10
    print('''
            6. How many ethnic groups do we have in Nigeria?
            A. 500
            B. 250
            C. 766
            D. 520
        ''')

    option = input('Answer: ').strip().capitalize()

    if option == 'B' :
        count += 10
    print('''
            7. Democracy day is celebrated on?
            A. June 10
            B. June 11
            C. June 12
            D. June 13
        ''')

    option = input('Answer: ').strip().capitalize()

    if option == 'C' :
        count += 10
    print('''
            8. What is the most populated country in the world?
            A. United State of America
            B. China
            C. India
            D. Russia
        ''')

    option = input('Answer: ').strip().capitalize()

    if option == 'B' :
        count += 10
    print('''
            9. The hottest region in the world is called?
            A. Sahel Desert
            B. Antantica Desert
            C. Indian Desert
            D. Sahara Desert
        ''')

    option = input('Answer: ').strip().capitalize()


    if option == 'D' :
        count += 10
    print('''
            10. Who formed the first political party in Nigeria?
            A. Herbert Macaulay
            B. Obafemi Awolowo
            C. Nnamdi Azikwe
            D. MKO Abiola
        ''')

    option = input('Answer: ').strip().capitalize()

    if option == 'A' :
        count += 10
    
    print(f'Thanks for taking the test {eachstudent}, your score is {count}\n')
    scorelist.append(count)

print(nameofstudents)
print(scorelist)

index_max = scorelist.index(max(scorelist))
print(f'Highest Score is {nameofstudents(index_max)}')