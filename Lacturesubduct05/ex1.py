#is_armstrong คือฟังก์ชันที่ใช้ตรวจสอบว่าตัวเลขที่กำหนดเป็น Armstrong number หรือไม่ Armstrong number 
#คือจำนวนที่เท่ากับผลรวมของตัวเลขแต่ละหลักยกกำลังด้วยจำนวนหลักของมันเอง ตัวอย่างเช่น 153 เป็น Armstrong number เพราะ 1^3 + 5^3 + 3^3 = 153
#โดย sum_of_powers คือผลรวมของตัวเลขแต่ละหลักยกกำลังด้วยจำนวนหลักของมันเอง และ return sum_of_powers == number จะคืนค่า True ถ้าตัวเลขเป็น Armstrong number และ False ถ้าไม่ใช่
#num_digits คือจำนวนหลักของตัวเลขที่กำหนด
#for digit in str_number คือการวนลูปผ่านแต่ละตัวเลขใน str_number และ int(digit) ** num_digits คือการยกกำลังของตัวเลขแต่ละหลักด้วยจำนวนหลักของมันเอง

def is_armstrong(number):
    str_number = str(number)
    num_digits = len(str_number)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_number)
    return sum_of_powers == number

print(is_armstrong(153))  # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))  # False