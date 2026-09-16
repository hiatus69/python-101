def divide (a,b):
    try:
        result = a/b
    except Exception as e:
        print("Error ",e)
    else:
        return result

a, b = map(int, input('enter two num: ').split())
print(divide(a,b))
print('end')