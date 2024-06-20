try:
    # Opens "DOB.txt" in readable mode
    with open('DOB.txt', 'r') as file:
        lines = file.readlines()

    # Initializes the variables to store the names and dates

    namesList = []
    datesList = []

    # Goes through each line to extract the names and dates
    for line in lines:
        # Splits the line into parts
        parts = line.strip().split(' ')
    
        # The first part is the names
        name = ' '.join(parts[:-3])
        # The rest is birth dates
        dates = ' '.join(parts[-3:])

        # Appends the name and date to their respective lists
        namesList.append(name)
        datesList.append(dates)

    # Print names and dates separately
    print("Name")
    for name in namesList:
        print(name)

    print("\nBirthdate")
    for dates in datesList:
        print(dates)

    file.close()

# Catches errors 
except (IOError,FileNotFoundError):
    print("Could not read file: DOB.txt")