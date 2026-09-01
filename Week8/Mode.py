def example_w_plus_mode():
    with open("example.txt", "w+") as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        # Move the file pointer to the beginning of the file
        file.seek(0)  
        content = file.read()
        print("Content of the file after writing:")
        print(content)

example_w_plus_mode()

def example_a_plus_mode():
    with open("example.txt", "a+") as file:
        file.seek(0)  # Move the file pointer to the beginning of the file
        content = file.read()
        print("Content of the file:")
        print(content)

        file.write("You think there is another line.\n")
        file.write("No, It me Dio.\n")
        # Move the file pointer to the beginning of the file
        file.seek(0)  
        updated_content = file.read()
        print("Content of the file after appending:")
        print(updated_content)

example_a_plus_mode()