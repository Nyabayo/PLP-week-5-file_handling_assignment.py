def create_and_write_file():
    try:
        # Creating and writing to the file
        with open('my_file.txt', 'w') as file:
            file.write('Hello, World!\n')
            file.write('This is a test file.\n')
            file.write('123456789\n')
    except Exception as e:
        print(f"An error occurred during file creation and writing: {e}")
    finally:
        print("File creation and initial writing complete.")

def read_and_display_file():
    try:
        # Reading from the file and displaying its contents
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except Exception as e:
        print(f"An error occurred during file reading: {e}")

def append_to_file():
    try:
        # Appending additional content to the file
        with open('my_file.txt', 'a') as file:
            file.write('Additional line 1\n')
            file.write('Additional line 2\n')
            file.write('Additional line 3\n')
    except Exception as e:
        print(f"An error occurred during file appending: {e}")
    finally:
        print("File appending complete.")

# Executing the functions in sequence
if __name__ == "__main__":
    create_and_write_file()
    read_and_display_file()
    append_to_file()
