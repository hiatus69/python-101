# #ฟังชันแบบไม่มีพารามิเตอร์
# def greet():
#     print("Hello, World!")
# greet()

# #ฟังชันแบบมีพารามิเตอร์
# def greet_user(name):
#     print(f"Hello, {name}!")
# greet_user("Alice")

# #ลำดับการเรียกใช้ฟังชัน
# def massaga():
#     print("I am Arthur")
#     print("King of the Britons")
    
# print('I have a massage for you.')
# massaga()
# print('Goodbye!')

#รวบรวมฟังชันและเรียกใช้ฟังชัน
# def main():
#     print('I have a massage for you.')
#     massaga()
#     print('Goodbye!')
# main()

# #return คือการส่งค่ากลับจากฟังชัน
# def add(a, b):
#     return a + b

# result = add(3,5)
# print(result)

# #ฟังชันแบบมีพารามิเตอร์แต่พารามิเตอร์มีค่าเริ่มต้น
# def greet_user(name="World"):
#     print(f"Hello, {name}!")
# greet_user()
# greet_user("Alice")

# #ฟังชัน sum() เป็นฟังชันที่ใช้ในการบวกตัวเลขหลายๆ ตัวเข้าด้วยกัน
# def sum_all(*args):
#     # total = 0
#     # for num in args:
#     #     total += num
#     # return total
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5))

# # เริ่มตรวจสอบ args ว่ามีค่าหรือไม่ ถ้าไม่มีค่าก็ return None 
# # และถ้ามีค่าก็ให้ max_value = args[0] จากนั้นวนลูปตรวจสอบค่าตัวเลขใน args 
# # ถ้าตัวเลขใดมากกว่า max_value ก็ให้ max_value = number สุดท้าย return max_value
# def find_max(*args):
#     if not args:
#         return None
#     max_value = args[0]
#     for number in args:
#         if number > max_value:
#             max_value = number
#     return max_value

# result = find_max(1, 5, 3, 9, 2)
# # result = find_max("banana", "apple", "orange") #ดูค่าตัวอักษรตัวแรกที่มากที่สุด
# print(result) 

# # enumerate() เป็นฟังชันที่ใช้ในการวนลูปผ่านลิสต์หรือออบเจ็กต์ที่สามารถวนลูปได้ 
# # และให้ค่าดัชนี (index) ของแต่ละองค์ประกอบในลิสต์หรือออบเจ็กต์นั้นด้วย
# def print_all(*args):
#     for index, arg in enumerate(args):
#         print(f"Argument {index + 1}: {arg}")

# print_all("python", 3.8, True, [1, 2, 3], {"key": "value"})

# # **kwargs เป็นฟังชันที่ใช้ในการส่งค่าพารามิเตอร์แบบไม่จำกัดจำนวนและไม่จำกัดชื่อพารามิเตอร์
# # items() เป็นฟังชันที่ใช้ในการวนลูปผ่านดิกชันนารีและให้ค่าคีย์และค่าของแต่ละองค์ประกอบในดิกชันนารีนั้นด้วย
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
# display_info(name="alice", age=30, city="New York")

# #len() เป็นฟังชันที่ใช้ในการนับจำนวนองค์ประกอบในลิสต์หรือออบเจ็กต์ที่สามารถวนลูปได้
# #max() เป็นฟังชันที่ใช้ในการหาค่ามากที่สุดในลิสต์หรือออบเจ็กต์ที่สามารถวนลูปได้
# #min() เป็นฟังชันที่ใช้ในการหาค่าน้อยที่สุดในลิสต์หรือออบเจ็กต์ที่สามารถวนลูปได้
# #sum() เป็นฟังชันที่ใช้ในการหาผลรวมของค่าตัวเลขในลิสต์หรือออบเจ็กต์ที่สามารถวนลูปได้
# def calculate_stats(numbers):
#     total_sum = sum(numbers)
#     average = total_sum / len(numbers)
#     maxinum = max(numbers)
#     minimum = min(numbers)
#     return total_sum, average, maxinum, minimum

# numbers = [5, 10, 15, 20, 25]
# total, avg, max_num, min_num = calculate_stats(numbers)

# # total, avg, max_num, min_num = calculate_stats([5, 10, 15, 20, 25])
# print(f"Total Sum: {total}")
# print(f"Average: {avg}")
# print(f"Maximum: {max_num}")
# print(f"Minimum: {min_num}")

# def my_function():
#     local_variable = "I am inside the function"
#     print(local_variable)
    
# my_function()
# # print(local_variable)  # This will raise an error because local_variable is not defined outside the function

# import random

# Head=1
# Tail=2
# Tosses=10

# def tosses_coin():
#     for toss in range(Tosses):
#         if random.randint(Head, Tail) == Head:
#             print("Heads")
#         else:
#             print("Tails")
# tosses_coin()

# #Global counter ทำให้สามารถเข้าถึงตัวแปร counter และแก้ไขได้จากภายในฟังก์ชัน increment() ได้ แต่ถ้าไม่ใช้ global counter จะทำให้เกิดข้อผิดพลาด UnboundLocalError เพราะ Python จะถือว่าตัวแปร counter เป็นตัวแปรท้องถิ่นภายในฟังก์ชัน increment() และไม่สามารถเข้าถึงตัวแปร counter ที่ประกาศไว้ภายนอกฟังก์ชันได้
# counter = 0
# def increment():
#     global counter
#     counter +=1
    
# increment()
# increment()
# increment()

# print(counter)  