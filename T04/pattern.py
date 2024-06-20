
rows = 5 #Sets the middle row with the most "*"

#Top Half of Pattern
for i in range(1, rows + 1):#loops for every row there is in the top half (increments the variable "i" by 1 until it reaches the set amount "rows+1" as "i" starts on 0)
    for j in range(1, i + 1):#loops to print a certain amount of "*" for each row
        print("*", end="")#prints "*" whilst staying on the same line after printing
    print()#moves to next line

#Bottom Half of Pattern
for i in range(rows - 1, 0, -1):#loops for every row there is in the bottom half (decrements the variable "i" by 1 until it reaches "0" as "i" starts on "rows+1"))
    for j in range(1, i + 1):#loops to print a certain amount of "*" for each row
        print("*", end="")#prints "*" whilst staying on the same line after printing
    print()#moves to next line

