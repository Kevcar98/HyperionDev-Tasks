def adding_up_to(num_list, index):
    if index == 0:
        return num_list[index] # Returns the first value in the list which has index 0
    elif 0 < index <= 4:
        return num_list[index] + adding_up_to(num_list, index - 1)
        #Returns recursively when the index is greater than 0 or less than or equal to 4
        # to then add the sum of the previous element
    else:
        return 0 
    
num_list = [1,4,5,3,12,16]
index = 4
print(adding_up_to(num_list, index))
print()

num_list_1 = [4,3,1,5]
index_1 = 1
print(adding_up_to(num_list_1, index_1))