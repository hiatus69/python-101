import struct
#define a record as a tuple
record = (1, 'John Doe', 20 , 3.75)
# Open a binary file for writing
with open("records.bin", "wb") as file:
    #pack the record into binary format and write it to the file
    data = struct.pack('i20sif',record[0],record[1].encode(),record[2],record[3])
    #wirte the binary data to the file
    file.write(data)
