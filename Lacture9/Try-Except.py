try:
    x= 1 / 0 #zero can't division error
except ZeroDivisionError as e: #you can only use except: 
    print(f"Error: {e}")