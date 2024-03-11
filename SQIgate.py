Students_db = [
    ('ADEBISI JOHNSON','FULL'),
    ('ADERIBIGBE EMMANUEL', 'NIL'),
    ('SIMON JOHN','PART'),
    ('OKORO DAVID', 'NIL'),
    ('STANLEY NWABILI', 'FULL'),
    ('ALEX IWOBI','NIL'),
    ('MOSES SIMON', 'PART'),
    ('ADEMOLA LOOKMAN', 'PART'),
    ('OLA AINA','FULL'),
    ('TROOST EKONG','FULL')
]

staff_db = [
    ('Femi', '21'),
    ('Yemi', '02')
]

Person = input('''
            WELCOME TO SQI COLLEGE OF ICT,
      Choose an option below to verify your identity:
      A. Staff
      B. Student
      C. Visitor
    Option: ''')


if Person.strip().capitalize() == 'A':
        staff_id = input('ID: ')
        staff_fname = input('First Name: ').strip().capitalize

        fnames = []
        IDs = []

        for fname, id in staff_db :
              fnames.append(fname)
              IDs.append(id)
        
        if staff_fname in fnames and staff_id in IDs :
            print('Access Granted👍, You can go in')
        else:
            print('Access Declined!')


elif Person.strip().capitalize() == 'C':
        print('You can proceed to the front desk')


elif Person.strip().capitalize() == 'B':
        print('Welcome to School, Input your name to verify your eligibility: \n')
        student = input('Your Name: ').strip().upper()
        
        Students_dbName =[]
        PaymentStatus=[]

        for name,payment in Students_db :
            Students_dbName.append(name)
            PaymentStatus.append(payment)

        if student in Students_dbName :
            print(f'\nWelcome {student}, kindly wait to verify your payment status\n')
        else:
            print('Your name is not registered')

        _index = Students_dbName.index(student)
        _status = PaymentStatus[_index]

        if _status == 'FULL' :
            print(f'{student}, you have made full payment, you can go in')
        elif _status == 'PART' :
            print(f'{student}, you have made half payment, pay up very soon to preserve your studentship')
        elif _status == 'NIL':
            print(f'You are not eligible to go in, return to your home')

