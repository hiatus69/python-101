fruit = ["apple", "banana","cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 1,6,9, 2.5,5, True]

print(fruit)
print(numbers)
print(mixed)
    
print("----------------------------------------")
#เลือกค่าตัวเลขที่ 5 จากลิสต์ numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(f"Prime numbers: {prime_numbers}")
fifth_primes = prime_numbers[4]
print(f"The fifth prime number is: {fifth_primes}")
print("----------------------------------------")
#เลือกค่าตัวเลขที่ 2 จากลิสต์ colors นับจากด้านหลัง
colors = ["red", "blue", "green", "yellow","purple"]
second_to_last_color = colors[-2]
print(f"The second to last color is: {second_to_last_color}")
print("----------------------------------------")
#modify list
shapes = ["circle","square","triangle","rectangle","pentagon"]
shapes[1]="ellipse"
shapes[2]="pentagon"
print(f"Modified shapes list: {shapes}")