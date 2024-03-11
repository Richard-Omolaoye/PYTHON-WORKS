# print('''Good day and trust you are doing fine
#       This is the Okoro Foundation Scholarship Test
#       How many students are you registering for the test?
#       Note: We dont take more than 5 students''')
# q_a=[]
# answer=[]
# cbt_question=[
#     ('1. Who is the present president of Nigeria? A. Goodluck Jonathan B. Muhammadu Buhari C. Nnamdi Azikwe D. Bola Ahmed Tinubu', 'd'),
#     (' 2. How many states are in Nigeria? A. 30 B. 32 C. 34 D. 36', 'd'),
#     (' 3. How many continents are in the world? A. 10 B. 6 C. 7 D. 8', 'c'),
#     ("  4. Who is the current president of the United States? A. Joe Biden B. Bill Clinton C. Barack obama D. Donald Trump")
# ]
# user = int(input('Number of Student: '))
# num_of_question = int(input('Number of Questions: '))
# nameofstudent = []
# questions=[]
# for x in range (1, user+1):
#     name = input(f'Name of Student {x}: ')
#     nameofstudent.append(name)
# for each_ques in range(1, num_of_question+1):
#     questions.append(num_of_question)
#     print('Welcome to the Okoro Foundation scholarship test, you have 5 minutes to answer the 10 questions and at the end of the test, your total score out of 100 will be displayed')
#     print('''
#                     Are you ready for the test?
#                 A. YES
#                 B. NO 

#                 ''')
#     count = 0
#     option = input('Option: ').strip().capitalize()
#     print(f'question {each_ques}')
#     for qa, ans in cbt_question:
#         # q_a.append(qa)
#         print(qa)
#         reply= input('enter your anser: ')
#         if reply == ans:
#             count += 10
#         if each_ques > num_of_question :
#             break
#         else:
#             print('bye')


# studentslist = []
# user = int(input('How many students are taking the test: '))

# for student in range(user):
#     stud = input(f'Name of Student {student+1}: ')
#     studentslist.append(stud)

# print(studentslist)

# numbers = [x for x in range (1, 21)]
# print(numbers)

# user = int(input('How many students are taking the test: '))
# studentlist =[input(f'Name of Student {student+1}: ') for student in range(user)]
# print(studentlist)

# for eachstudents in studentlist:
#     print(f'{eachstudents} its time for your test')

#     score = 0
#     question = [
#         '1. What is the capital of Nigeria a.) Oyo b.) Abuja',
#         '2. What is the capital of Japan a.) Tokyo b.) Abuja'
#     ]
#     answer = ['b', 'a']

#     for ques, ans in zip(question, answer):
#         print(ques)

#         user = input('Answer: ')
#         if user.strip().lower() == ans :
#             print('Correct')
#             score+=5
#         else:
#             print('Why u no know book')

    # print(f' Your total score is {score}')
# user = int(input('How many workers do you have in the company: '))
# workers = [input(f'Name of workers {worker+1}:') for worker in range (user) ]
# print(workers)
    
# items = ['Bag', 'Shoe']
# prices = [1000, 2000]
# for x,y in zip(items, prices):
#     print(f'{x}---{y}')

# count = 5
# Order = (input(f'foods {x+1}: ') for x in range (count))
# print(Order)


    
number = int(input('How many students are taking the test: '))
students = [input(f'Name of Students {x+1}:') for x in range (number)]

scorelist = []

for eachstudent in students :
    print(f'{eachstudent}, it is time for your test\n')

    score = 0
    questions = [
        '1. How many states are in Nigeria \nA. 23  \nB. 36  \nC. 30',
        '2. Who is the president of United State \n A. Bil Clinton  \nB. Anthony Martial  \nC. Joe Biden',
        '3. Who discovered Neutron \nA. Chadwick \n B. Rutherford \nC. Mosley',
    ]
    answers = ['C', 'C', 'A']

    for ques, ans in zip(questions, answers):
        print(ques)

        user = input('Answer: ')
        if user.strip().capitalize()== ans :
            print('Correct')
            score+=5

    print(f'Thank you for taking the test, your score is {score}\n')
    scorelist.append(score)

print(students)
print(scorelist)

print(max(scorelist))