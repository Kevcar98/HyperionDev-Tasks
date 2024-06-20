
# This function uses the num_nights variable to return the calculation of the total cost of the hotel
def hotel_cost(num_nights):
    price = 125
    total_cost = price * num_nights
    return total_cost

# This function uses the city_flight variable to return the calculation of the total cost of the plane
# by determining which city is the destination
def plane_cost(city_flight):
    # Makes a new variable lower where it stores the string stored in city_flight into all lower case to be then compared
    lower=city_flight.lower()
    if(lower == "london"):
        price = 150
    elif(lower == "tokyo"):
        price = 325
    elif(lower == "paris"):
        price = 175
    else:
        price = 100
    total_cost = price
    return total_cost

# This function uses the rental_days variable to return the calculation of the total cost of the rental
def car_rental(rental_days):
    price = 74
    total_cost = price * rental_days
    return total_cost

# This function uses the num_nights,city_flight,rental_days variables to return the calculation of the total cost of the hoiliday
def holiday_cost(num_nights,city_flight,rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)


def main():

    # Gets the city destination from the user input
    city_flight=input("Enter the city you will be flying to: ")

    # The while loop below will loop until the correct type of input is inputted and will catch any errors
    while True:
        try:
            
            num_nights=int(input("Enter the number of nights you'll be staying at the hotel: "))              
            break
        except ValueError:
            print("The input was not a valid number.")
    
    # The while loop below will loop until the correct type of input is inputted and will catch any errors
    while True:
        try:

            rental_days=int(input("Enter the number of days you'll be hiring a car: "))         
            break
        except ValueError:
            print("The input was not a valid number.")

    # Gets the return value of the holiday_cost function by getting final_hotel_cost, final_plane_cost, final_car_rental variables into the variable final_cost
    final_cost=holiday_cost(num_nights,city_flight,rental_days)
    print("The total cost of the hotel, the plane and the car rental is "+str(final_cost)+" for you journey to "+city_flight+" of "+str(num_nights)+" nights.")

if __name__ == "__main__":
    main()


    