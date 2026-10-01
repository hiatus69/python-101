import struct

num_records = int(input("Enter the number of records: "))

with open("records.bin", "wb") as file:
    for i in range(num_records):
        # get data from user
        id_num = int(input(f"Enter ID for record : "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gpa = float(input("Enter GPA: "))

        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)
        file.write(data)
print(f"{num_records} records written to records.bin")