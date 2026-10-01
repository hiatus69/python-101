numbers = [4,2,9,1,5,6]

length = len(numbers)
print(f"len {length}")
total_sum = sum(numbers)
print(f"sum {total_sum}")
max_value = max(numbers)
print(f"max {max_value}")
min_value = min(numbers)
print(f"min {min_value}")
sort_number = sorted(numbers)
print(f"sorted {sort_number}")

bool_list = [False,True,False]
any_true = any(bool_list)
print(F"ANY IS TRUE? : {any_true}")

all_true = all(bool_list)
print(f"all are true? : {all_true}")

string = "hello"
char_list = list(string)
print(f"List : {char_list}")

reversed_nunbers = list(reversed(numbers))
print(f"reversed list : {reversed_nunbers}" )

enumerate_numbers = list(enumerate(numbers))
print(f"Enumerated list : {enumerate_numbers}")