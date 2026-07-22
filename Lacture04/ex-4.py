# column = int(input('แถวที่อยากได้'))

# for num in range(2,100,1):
#     print(num ,end=" ")
#     if num % column == 0:
#         print()

# row = int(input('แถวที่อยากได้'))
# row = 100//row


# for num in range(1,101,1):
#     print(num ,end=" ")
#     if num % row == 0:
#         print()

#ไม่ผ่าน
row = int(input('แถวที่อยากได้'))
count = 1
for i in range(1,20,1):
    for num in range(row):
        if count > 100 :
            break
        print(count ,end=" ")
        count += 1
    if count > 100:
        break
    print()