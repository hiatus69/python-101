# column = int(input('แถวที่อยากได้'))

# for num in range(2,100,1):
#     print(num ,end=" ")
#     if num % column == 0:
#         print()

row = int(input('แถวที่อยากได้'))
row = 100//row

for num in range(2,101,1):
    print(num ,end=" ")
    if num % row == 0:
        print()
