# print("Hello World")
# print("My name is Richard")

# '''
# fghjk
# dfghjkldsjshgfgdfsghjk
# tyduiskjbvfcdtyujk
# dfyujikkjhfcyujkjghgh
# '''

# print("Data Science is a great course at SQI")
# print("If you dont believe, you have to come")

x=5
y=10

# print(x+y)
# print(x*y)
# print(x-y)
# print(y/x)
# print(x%y)
# print(x//y)
# print(x**y)

val1 = bin(30)
val2 = bin(50)

# print(val2)

# a = 7
# b = 8

# print(a+b)

# firstname = 'Richard'
# lastname = 'Oluwatimilehin'
# print(f'My name is {firstname}')
# print(f'I am also called {lastname}')
# print(f'{lastname} {firstname}')

# CONCATENATION METHODS
first_name = 'Richard'
last_name = 'Oluwatimilehin.'
age = 80
# COMMA
# print( 'My name is', first_name,last_name,'I am', age, 'year old')
# ADDITION SIGN
# print( 'My name is ' +first_name+ ' ' +last_name+ ' I am ' +str(age)+ ' years old')
# F STRING
# print(f'My name is {first_name} {last_name} I am {age} years old.')

# PYTHON DATA TYPES
'''
1. Text Type; strings, str() e.g 'Banana' '55'

2.  Number types;
        Integers, int() e.g 45, 6
        Float, float() e.g 45.4, 4.007
        Complex numbers

'''

# val = ['Banana', 'Adebayo', True, 65, 3+5j]
# value = ['Olu', 'Boro',False, 'Ewo', 78]
# val.append(value)
# val2 = val.extend(value)
# val.insert(5, 'Obamide')(Takes two argument)
# val.pop(0)
# val.remove('Banana')
# print(val.index(True))
# val.clear()
# val.reverse()
# val.sort()
# print(val)


# print(len(val))
# print(type(val))
# print(val[4])

# print('''
#             MY ALATA CALCULATOR
#       1. Addition
#       2. Subtraction
#       3. Division
#       4. Multiplication

#     ''')

# user = input('Option: ')
# first_value = input('First Value: ')
# second_value = input('Second Value: ')

# if user == '1' :
#     res = first_value+second_value
#     print('Answer: ',res)

# elif user == '2' :
#     res = first_value - second_value
#     print('Answer: ',res)

# # PYTHON ESCAPE CHARACTERS
# expression = ('This is my python file path - C:\python_feb\new_file\read_python\think_python')
# # SOLUTION - Double slash or (r) before string
# # print(expression)

# # \t tab
# print('I am a \t\t\t genius')

# # \b backspace
# print('I am a \b\b\b genius')

# # \n enter
# print('I am a\n\n genius')

# # \r
# print('I am a\r genius')

# PYTHON COLLECTIONS
'''
1.  LIST [] or list()
    Properties of a Class List
        i.  Ordered
        ii. Changeable/Mutable
        iii.It allows duplicate values
        iv. It can be indexed
'''

# my_list = ['Maimunat', 'Joshua', 45, True, ['Yam', 'Rice', 'semo'], 'Bottle']
# print(len(my_list))
# print(my_list[0])
# print(my_list[-4])
# print(my_list[-2][-2])
# print(my_list[5][1])

# SLICING
# print(my_list[2:])
# print(my_list[4:6])

# my_list[0] = 'Mary'
# print(my_list)

# my_list[0:3] = 'Tolu','Marv','Dave'
# print(my_list)

# FUNCTIONS A LIST CLASS CAN PERFORM
li = []
# print(li)

# li.append('Habeeb')
# li.extend(['habeeb','dave'])
# print(li)

# my_list.clear()
# del my_list
# print(my_list)

# print(my_list.count('Joshua'))
# print(my_list.index('Joshua'))

# my_list.pop()
# print(my_list)

# my_list.pop(3)
# print(my_list)

# my_list.remove(45)
# print(my_list)

# my_list.reverse()
# print(my_list)

# my_list.sort() - Learn
# print(my_list)

# my_list.insert(0, 'Richard')
# print(my_list)

# num = [20, 15, 34, 10]
# print(sum(num))
# print(max(num))
# print(min(num))

# python_students = ['Tolu', 'Joshua', 'Mary', 'Maimunat', 'Marv']
# for each in python_students : 
# #     print(each)
#     print('Welcome to class', each)

# questions = ['''
#           WELCOME

#             1. Who is the present president of Nigeria?
#         A. Goodluck Jonathan
#         B. Muhammadu Buhari
#         C. Nnamdi Azikwe
#         D. Bola Ahmed Tinubu
#     ''']

# for each_quest in questions:
#         print(each_quest)
#         user = input('Answer: ')

# num = []
# for x in range(10):
#         num.append(x)
# print(num)

# Name_of_Student = []
# for x in range (10):
#         name = input(f'Name {x+1}: ')
#         Name_of_Student.append(name)
   
# print(Name_of_Student)

# # ASSIGNMENT
# Ask your user the number of students who want to take your test
# Learn about function zip
# Do another version of your CBT question with a list
# Call/Invite students to take their test and choose the student with the max score

# TUPLE () tuple()
'''
1. Unchangeable/immutable
2. Indexed
3. Allow duplicate value
4. Ordered
Sensitive information are kept in a tuple
''' 

students = ('Damilare', 'Slessor', 'Maimunat', 'Richard', 23, True, [23, 24, 'Wale'], ('Samuel', 34))
# print(students[3])
# print(students[-3])
# print(students[1: 4])

# list_students = list(students)
# # print(list_students)
# list_students[1] = 'Mary'
# # print(list_students)

# students = tuple(list_students)
# print(students)

# # UNPACKING
# *list_students, = students
# print(list_students)

# student1, student2, student3, student4, *alls = students
# *student1, student2, student3, student4, alls = students
# print(student1)
# print(alls)

# print(students.count('Slessor'))
# print(students.index('Richard'))

# student = ['Ayo', 'Bayo', 'Fola', 'Femi']
# scores = [30, 60, 40, 50]
# index_max = scores.index(max(scores))

# print(student[index_max])

# mean_score = sum(scores)/len(scores)
# print(mean_score)

# names = ('Mary', 'Lola', 'Ayo', 'Femi')
# scores =(23, 45, 95, 65)
# # for name in names :
# #     print(name)
# #     print('___________________')

# for name, score in zip(names, scores) :
#     print(f'{name} scored {score}.')

# details = [
#     ('mary', 23),
#     ('Lola', 45),
#     ('Ayo', 95),
#     ('Femi', 65)
# ]

# for name,score in details :
#     print(f'{name} scored {score}')
# print(details)

# score = 0
# Questions = [
#     ('1. How many states are in Nigeria \nA. 23  \nB. 36  \nC. 30\n', 'B'),
#     ('2. Who is the president of United State \nA. Bil Clinton  \nB. Anthony Martial  \nC. Joe Biden\n', 'C'),
#     ('3. Who discovered Neutron \nA.Chadwick \nB. Rutherford \nC. Mosley\n', 'A'),
#     (' 4. How many continents are in the world? \nA. 10 \nB. 6 \nC. 7 \nD. 8 \n', 'C'),
#     ('5. Who is the present president of Nigeria?\nA. Goodluck Jonathan \nB. Muhammadu Buhari \nC. Nnamdi Azikwe \nD. Bola Ahmed Tinubu\n', 'D'),
# ]

# for question, answer in Questions:
#     print(question)
#     user = input('Answer: ').strip().capitalize()
#     if user == answer :
#         print('Correct\n')
#         score += 10
#     else:
#         print('Wrong\n')    
        
# print (f'You scored {score}')

# FOR LOOP iterates on a condition
# WHILE LOOP

# x = 1
# while x == 1 :
#     print('Yes')
    # x+=1

# user = input('USSD: ').strip()
# while user != '*321#' :
#     print('Invalid ussd code. Try again')
#     user = input('USSD: ').strip()
# print('Welcome to myMTN')     

# slot = 10
# admission_list = []
# while slot >= 1 :
#     name = input('Aspirant Name: ')
#     admission_list.append(name)
    
#     slot -= 1
# else:
#     print(admission_list)

x = 1  
# while True :
#     print(x)
#     x += 1
#     if x==10:
#         continue

#     if x==20:
#         break


# Ticket = 10
# while Ticket >= 1 :
#     age = int(input('Age: '))
#     Ticket -= 1
#     if age<18 :
#         continue
#     else:
#         print(Ticket)

# SUPERMARKET
# Take their name
# Available goods
# Check if it is in the list
# Produce a receipt with the price
# Ask if they still want another order

# print('''
#     Thanks Mr Dami. Your orders are
#       1. Nike Sneekers --> #20,000
#       2. Rolex --> #30,000

#         Total = #50,000

# ''')


# SET {}  direct opposite of list
    
'''
    1. Unchangeable/Innutable
    2. It cant be indexed
    3. It is not ordered
    4. It does not allow duplicate value
    '''

# myset = {'apple', 'pineapple', 'orange', 'cherry'}
# # # print(type(myset))
# # print(myset)
# # setnum ={5,4,7,6,9,3,2,1,8}
# # print(setnum)

# # FUNCTIONS
# # myset.add('watermelon')
# # myset.update(['yam', 'beans'])
# # print(myset)
# # fruits = myset.copy()
# # myset.pop()
# # print(fruits)
# # print(myset)
# balance = 500
# stake = float(input('stake: '))
# while balance > 0 and balance > stake :

#     guess = input('Guess the outpit: ').strip().lower()
#     chosen_fruit = myset.pop()
#     myset.add(chosen_fruit)

#     if guess == chosen_fruit:
#         balance +=2 *stake
#         print(f'You guesses right. Your current balance is {balance}')
#     else:
#         balance -= stake
#         print(f'Wrong, your balance is {balance}')

#         user = input('Press 1 to replay or # to exit')
#         if user == '#' :
#             break
#         else:
#             print('Insufficient Fund.')

# print(f'Your cashout balance is {balance}')


setA = {5, 4, 7, 6, 9, 3, 2, 1, 8, 10, 11}
setB = {3, 2, 4, 5, 6,5,4}

# print(setA.union(setB))
# print(setA.intersection(setB))
# setA.intersection_update(setB)
# print(setA)
# print(setA.difference(setB))
# print(setA-setB)
# setA.symmetric_difference(setB)
# print(setA)
# setA.isdisjoint 

# do a calculator that can perform set operations

#Dictionary {they are always in keys and values},   {key:value}, dict{key=value}
'''
1. It is changeable
2. It is ordered
3. Duplicate is not allowed
'''

# car = {'Model':'Tesla', 'Year':2020}
# # print(car)
# # print('The model is',car['Model'])
# car['Model'] = 'Benz'
# print(car)

# car = {
#    'Model':'Tesla',
#    'Year':2022,
#    'color':['Black','Blue'],
#    'owner':{
#       'name': 'Dami',
#       'price': 23435
#    }
# }
# print(car['color'][0])
# print(car['owner']['name'])

# print(car.items())