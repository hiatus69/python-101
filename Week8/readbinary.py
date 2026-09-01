import struct

# with open("records.bin", "rb") as file:
#     #read the binary data from the file
#     data = file.read(struct.calcsize('i20sif'))
#     #unpack the binary data into a record
#     record = struct.unpack('i20sif', data)
#     #decode the name from bytes to string and remove any null bytes
#     record = (record[0], record[1].decode().rstrip('\x00'), record[2], record[3])
#     print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]}")

record_format = 'i20sif'
record_size = struct.calcsize(record_format)

with open("records.bin", "rb") as file:
    file.seek(record_size)  # Move the file pointer to the second record
    data = file.read(record_size)#read the binary data for the second record
    record = struct.unpack(record_format, data)#unpack the binary data into a record
    record = (record[0], record[1].decode().rstrip('\x00'), record[2], record[3])#decode the name from bytes to string and remove any null bytes
    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]}")#print the second record