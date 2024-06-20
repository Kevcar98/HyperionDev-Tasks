
num=""#Creates an empty String variable called "num"
total=0#Creates an integer variable called "total"
count=0#Creates an integer variable called "count"
while True:#Makes an infite loop
    try:#to catch any errors due to the "num" not being a valid integer
        while num != "-1":#A while loop that loops when "num" variable is not equal to "-1"
            num = input("Input a number:")#stores the user input into the variable "num"
            if num != "-1":#if statement to make sure "num" is not equal to "-1"
                total+=int(num) #the variable "total" stores the total of the current total with new number stored in "num"
                count+=1#a counter that increments by 1
        break#breaks the "while True:" loop  
    except ValueError:#catches the error "ValueError" caused by the input of the user in they entered something that wasnt a compatible integer value
        print("The input was not a valid integer.")#prints message
if count != 0:#if statement that makes sure that count is not equal to 0 as you need at least one number to find an average and you can't divide by 0.
            print("The average of all your number is: "+str(total/count))#prints the average of all the numbers the user has input
