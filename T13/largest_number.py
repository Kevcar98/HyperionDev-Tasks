list_1 = [1, 4, 5, 3]
list_2 = [3, 1, 6, 8, 2, 4, 5]

def largest_number(chosen_list):
    # If the list has only one element
    if len(chosen_list)==1:
        return chosen_list[0]
    else:
        # Finds the largest number in the sublist excluding the first element
        big_number = largest_number(chosen_list[1:])

        # Compares the element to the current biggest number
        if chosen_list[0]>big_number:
            return chosen_list[0]
        else:
            return big_number


print(largest_number(list_1))
print()
print(largest_number(list_2))
