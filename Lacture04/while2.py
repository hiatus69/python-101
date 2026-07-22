keep_going='y'

while keep_going == 'y':
    
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commssion rate: "))
    
    commission = sales * comm_rate
    
    print(f'The commission is ${commission:.2f}')
    
    keep_going = input('Do you wnt to calculate another' + \
        ' commission (Enter y for yes): ')
    keep_going = keep_going.lower()