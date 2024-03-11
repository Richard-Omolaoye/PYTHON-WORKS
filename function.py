#FUNCTIONS
'''A function is a block of code that is assigned to do a specific task
We have parametrize and non parametrize functions
to define our function, we use the key word unparametrized function
'''
'''python declaration
initialize or define then yiu
invoke it'''
#unparametized function
# def addition():
#     value1 = int(input('Enter first value: '))
#     value2 = int(input('enter second value: '))
#     result = value1+value2
#     print(f'ans: {result}')
# addition()

#parametize function
# def addition (value1, value2 =10):
#     result = value1 + value2
#     print(f'ans: {result}')

# addition(value1=int(input('Enter the first value: ')))
# addition(4, 8)

val1 = 12
def addition (val3):
    global val2
    val2 = 10
    result = val1 + val2 + val3
    print(f'ans: {result} nice')
    # subtraction()
    
# def subtraction():
#     results = val1 - val2
#     print(f'ans: {results} amazing')
# addition(int(input('enter value: ')))

#Calculator


   
# name = 'slessor'
# def know_me():
#    global occupation
#    occupation = 'Data science'
#    print(f'My name is {name}. And my occupation is {occupation}.')
# know_me()

# def describe():
#    print(f'My work is {occupation}')
# describe()



# def landing_page(): 
#     global value1
#     global value2
#     name = input('Name: ')
#     value1 = float(input('Value 1: '))
#     value2 = float(input('Value 2: '))
#     user = input(f''' My alata calculator. \n Welcome {name}.
#       1. Addition
#       2. Subtraction
#       #. Exit
#     Choose your operation:  ''').strip()
#     if user == '1':
#         addition()
#     elif user == '2':
#         subtraction()
#     elif user == '#':
#         exit()
#     else:
#         print('Invalid input')
#         landing_page()
        
# def addition():
#     print(f'Ans: {value1 + value2}')
#     decide()

# def subtraction():
#     print(f'Ans: {value1 - value2}')  
#     decide()

# def decide():
#     user = input('Press 1 to go to home or enter to exit: ')
#     if user == '1':
#         landing_page()
#     else:
#         exit()    


# landing_page()     

# def add(val1: float, val2: float = 10):
#     '''(it's called docstring)
#     I add things up
#     '''
#     return val1 + val2

# def arithmetic():
#     res = 2 ** add(10)
#     return{res}
# def printf(name):
#     print(f'{name}, your result is {arithmetic()}')
    
# printf(input('Your name: '))
# cbt and ussd use function


# class Dust:
#     def __init__(self):
#         self.first_name1 = 'Arise'
#         self.last_name1 = 'Damilare'
#         self.age = ''
        
#         self.naming()
        
#     def naming(self):
#         print(f'My name is {self.first_name1} {self.last_name1}')

# father = Dust()
#oop(object oriented programme )
    

# Declaration
# Definition
# Invocation

# Global Function  
surname = 'Ojo' 

# UNPARAMETIZED
# def call_name(): 
#     name = input('First Name: ').strip()
#     print('My name is', name)
# call_name()


# PARAMETIZED
# def call_name(name:str):
#     print('My name is', name)
# x = input('First Name: ')
# call_name(x)


# class Calculator:
#     def __init__(self):
#         self.calc_name ='Casio'

#         self.home()
val1=3
def add():
    val3=6
    global val4
    val4=10
    val2=int(input("enter value two "))
    result=val1+val2+val3
    # oruko=name
    print(result, 'excellent')
    sub()

    



def sub():
    val2=int(input("enter value two "))
    result=val2-val1-val4
    
    print(result, "good")
#     def home(self):
add()

#         print(f'Welcome to {self.calc_name}')
#         self.value1 = float(input('Input your first value: '))
#         self.value2 = float(input('Input your second value: '))
#         user = input ('''
#             Choose your operation:
              
#               1. Addition
#               2. Subtraction
#               #. Exit
#         Option: ''')

#         if user == '1':
#             self.addition()
#         elif user == '2':
#             self.subtraction()
#         elif user == '#':
#             exit()
#         else:
#             print('Invalid Option, Try again!')
#             self.home()

#     def addition(self):
#         print(f'ANS: {self.value1 + self.value2}')
#         self.decide()

#     def subtraction(self):
#         print(f'ANS: {self.value1 - self.value2}')
#         self.decide()

#     def decide(self):
#         user = input('Press 1 to home or # to exit: ')
#         if user == '1':
#             self.home()
#         else:
#             exit()

# casio = Calculator()
# casio.home()

# INHERITANCE

# class parent:
#     def __init__(self) -> None:
#         self.surname ='Ojo'
#         self.firstname = 'Mary'
#         self.hobby = 'Eating'

#         self.describe()

#     def describe(self):
#         print(f'My name is {self.surname} {self.firstname}, I love {self.hobby}')

# Parent = parent()
# # print(Parent.surname)

# class child(parent):
#     def __init__(self):
#         parent. __init__(self)
#         self.firstname = 'Maimunah'
#         self.hobby = 'Sleeping'
#         self.bestfood = 'Fufu & Egusi'

#         self.describe()

#     def cooking(self):
#         print(f'{self.firstname} is cooking {self.bestfood}')

# Child =child()
        
# class grandchild(child):
#     def __init__(self):
#         super().__init__()
#         self.firstname = 'Richard'
#         self.hobby = 'Talking'

#         self.describe()

# Grandchild = grandchild()


# SCRIPT = Python script (.py file)
# MODULE = Any python script with one or more class inside of it
# LIBRARY = A folder with different modules in it


# SQL IS A LANGUAGE FOR STRUCTURED DATA (SQLlite, mySQL, postgreSQL, msSQL, Oracle uses the language SQL)
# JSON IS A LANGUAGE FOR UNSTRUCTURED DATA
# mySQL
# XAMPP - Cross Apache MySQL php Perl