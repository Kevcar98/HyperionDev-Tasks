# Loops until an integer value is given
while True:            
    try:
        StudentNum=int(input("How many students are being registered for the exam venue? "))
        break
    except ValueError:
        print("The input was not a valid number.")

# Loops for the amount of users to be registered
for i in range(StudentNum):
    UserID=input("Enter Student ID: ")

    try:
        # Appends the necessary data to the text file if the file already exists
        with open('reg_form.txt', 'a') as file:
            file.write(UserID+"\n")
            file.write("...................................\n")
            #If you meant the other way then:
            #file.write(UserID+"...................................\n")
    except FileNotFoundError:
        # If the file doesn't exist, then it is created and we use write mode to add data to it
        with open('reg_form.txt', 'w') as file:
            file.write(UserID)
            file.write("...................................")
            #If you meant the other way then:
            #file.write(UserID+"...................................")
