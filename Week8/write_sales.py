num_days = int(input("Enter the number of days: "))
#write w เขียนทับ a เขียนดพิ่ม
with open("sales.txt", "a") as sales_file:
    for count in range(1, num_days + 1):

        sales = float(input(f'Enter the sales for day #{count}: '))
        sales_file.write(str(sales) + "\n")

print("Data written to sales.txt")
#read
with open("sales.txt", "r") as sales_file:
    for line in sales_file:
        amount = float(line)
        print(f"Sales amount: {amount:.2f}")