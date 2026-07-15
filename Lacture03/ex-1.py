test1 = int(input("Enter your score test 1: "))
test2 = int(input("Enter your score test 2: "))
test3 = int(input("Enter your score test 3: "))

average_score = (test1 + test2 + test3) / 3

print("Your average score is:", format(average_score, ".1f"))
if average_score > 95:
    print("Congratulations! \nThat is a great average!")
    