student = {"name":'Alice','age':25,'grade':'A','Major':'Computer Science'}

for key in student:
    print(f"{key}: {student[key]}")

for e in student.values():
    print(e)

for i, value in student.items():
    print(f"{i}: {value}")