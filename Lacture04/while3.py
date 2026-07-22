keep_going='y'

while keep_going == 'y':
    
    Wholesale_cost = float(input("Enter the item's Wholesalecost: "))
    retail_price = Wholesale_cost*2.5
    print("Retail price: $",retail_price)
    
    keep_going = input('Do you wnt to calculate another' + \
        ' commission (Enter y for yes): ')
    keep_going = keep_going.lower()