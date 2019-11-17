# Test whether fridge temperatures are between 1 and 5 degrees Celsius

# function with one parameter, temperatures: a list of numbers

def test_temperature(temperatures):

    # initialise empty list to store temperatures outside of range 1 to 5 

    unacceptable_temperatures = []

    # iterate through input list 

    for temperature in range(len(temperatures)):

        # filter unacceptable temperatures outside of range 1 to 5
        
        if temperatures[temperature] < 1 or temperatures[temperature] > 5:

            # append temperature to list of unacceptable temperatures

            unacceptable_temperatures.append(temperatures[temperature])

    # output list of unacceptable temperatures

    print(unacceptable_temperatures)

# check that test_temperatues works

def check_test_temperatures():

    assert test_temperatures([1,2,3,4,5]) == []
    assert test_temperatures([-1,2,4,6]) == [-1,6]
