#variable int to float
age = 22
height = float(age)
print("height:", height)

#float to int
height = 5.9
age = int(height)
print("age:", age)

#str to int
num_str = "123"
num_int = int(num_str)
print("num_int:", num_int)

# set={1, 2, 3}
# intset = int(set)
# print(intset)
#ไม่สามารถแปลง set เป็น int ได้โดยตรง เพราะ set เป็น collection ของค่าที่ไม่ซ้ำกันและไม่มีลำดับ การแปลงเป็น int จะไม่สามารถทำได้โดยตรง
# list1 = [1, 2, 3]
# intlist = int(list1)
# print(intlist)
#ไม่สามารถแปลง list เป็น int ได้โดยตรง เพราะ list เป็น collection ของค่าที่มีลำดับ การแปลงเป็น int จะไม่สามารถทำได้โดยตรง