import time
Students_db = [
            ('Ojo Mary', 'Paid'),
            ('Johnbull Paul', 'Half Paid'),
            ('Simon Peter', 'Half Paid'),
            ('James Peter', 'Unpaid'),
            ('John Jude', 'Half Paid'),
            ('Philip Andrew', 'Unpaid'),
            ('Judas Carrot', 'Unpaid'),
            ('Michael Gabriel', 'Paid'),
            ('William Saliba', 'Unpaid'),
            ('Mikel Arteta', 'Paid')

        ]

staff_db = [
            ('Femi', '21'),
            ('Yemi', '02'),
            ('Bayo', '03'),
            ('Dayo', '04'),
            ('Titi', '05')
        ]

class SQI :
        def __init__(self):
            self.SQI = 'SQI Entrance'

            self.home()

        def home(self):
            user = input('''Welcome to SQI College of ICT
                        VERIFY YOUR IDENTITY
                        1. Staff
                        2. Student
                        3. Visitor
                        Option: ''')
            if user == '1':
                self.staff()
            elif user =='2':
                self.student()
            elif user =='3':
                self.visitor()
            
        def staff(self):

            snames =[]
            sids =[]

            for sname,sid in staff_db:
                snames.append(sname)
                sids.append(sid)

            userid = input('Your ID Number: ')
            username = input('Your Name: ').strip().capitalize()
            if userid in sids and username in snames:
                print(f'Access Granted, Welcome to work {username}')
            else:
                print('Access Denied, you are not on the staff database')

        def student(self):

            names = []
            payments = []

            for name,payment in Students_db:
                names.append(name)
                payments.append(payment)

            Name = input('Your Name: ').title()
            if Name in names:
                print(f'Welcome to School {Name}, wait to verify your payment')
                pay_index = names.index(Name)
                time.sleep(3)
                if payments[pay_index] == 'Paid':
                    print('You have made full payment, can go in')
                elif payments[pay_index] == 'Half Paid':
                    print('You made half payment, visit the front desk for clarification')
                elif payments[pay_index] == 'Unpaid':
                    print('You have made no payment, please go back home')
            else:
                print('Your name is not on the school student database')
                
        def visitor(self):
            print('Welcome to SQI, please visit the front desk')

SQIgate = SQI()
    