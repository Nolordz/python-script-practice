menu = """
******************************
 PROJECT 7 - MENU
******************************
1. Write input to file
2. Write input to screen
3. Quit
******************************
Enter a number [1-3]:
"""
user_option = raw_input(menu)
while user_option == "1" or user_option == "2":
    if user_option == "1":
        file_name = raw_input("Enter a file name: ")
        with open(file_name, 'w') as f:
            f.write(raw_input("Enter a phrase"))
    elif user_option == "2":
     user_option = raw_input(menu)
else:
    print ("Thank you for playing")
    exit()







