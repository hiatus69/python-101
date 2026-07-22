rows = int(input("enter row: "))
columns = int(input("enter column: "))

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()