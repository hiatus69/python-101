matrix = [
    [1,10,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    print(row,2)
    for element in row:
        print(element, end="")
    print()

# import random
# ROWS = 3
# COLS = 4

# def main():
    
#     values = [
#         [0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]
#     ]
    
#     for r in range(ROWS):
#         for c in range(COLS):
#             values[r][c]= random.randint(1,100)
            
#     print(values)
    
# main()