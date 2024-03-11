print('''Good day respected customer,
      Welcome to B & B Supermarket,
      What would you love to buy''')

Basic_needs = [
        ('Rice', 75000),
        ('Beans', 60000),
        ('Spaghetti', 5000),
        ('Milk', 1000),
        ('Orange', 200),
        ('Phone', 50000),
        ('Lamp', 4000),
        ('Bag', 10000),
        ('Cloth', 12000),
        ('Cream', 5000),
        ('Book', 4000),
        ('Shoe', 15000)
]

Purchases =[]
while True: 
        print(goods)
        Item = input('Input the item you want: ').strip().capitalize()
        for goods,price in Basic_needs :
                if Item in goods:
                        Quantity = int(input(f'Input the Quantity of {Item}: '))
                        Purchases.append((Item, Quantity))
                        More = input('Do you want more (yes/no): ').strip().capitalize()
                        if More != 'Yes':
                                break
                else:
                        print('Sorry, the Item is not available')

        name = input('Input your name to get your receipt: ')

        TotalCost = 0
        for purchase,quantity in Purchases:
                Price = Basic_needs[purchase]
                cost = Price*quantity
                TotalCost += cost

                print(f'''{name} ,Thank you for patronizing us,
                Your purchases are {Purchases},
                Your total price is {TotalCost} 
                        ''')












