#slice list
data = list(range(100))
slice = data[10:51:5]
print(f"slice data is :{slice}")
print("--------------------------------------------")
number = [0,1,2,3,4,5,6,7,8,9]

print(number[2:6])
print(number[1:8:2])
print(number[:4])
print(number[6:])
print(number[-5:-1])
print(number[::-1])
print("--------------------------------------------")

name = "Sammy Shark!"

print(name[4])
print(name[6:11])
print(name[:5])
print(name[7:])
print(name[-4:-1])
print(name[6:11])
print(name[6:11:1])
print(name[0:12:2])
print(name[0:12:4])
print(name[::4])
print(name[::-1])
print(name[::-2])
print("--------------------------------------------")
even_number = [2,4,6,8,10]
heroes = ['thor','ironman','spiderman','hulk']
numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[-5:])
number[8] = 99
print(numbers)

pluslist = heroes + even_number 
print(pluslist)
print(len(numbers))