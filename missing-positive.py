def first_missing_positive(numbers):
    # Check if numbers is not empty and get the max_value
    if numbers:
        max_value = max(numbers)
    else:
        max_value = 0 

    # If max_value is less than 1 : return 1 
    if max_value < 1:
        return "The first missing positive number is: 1"

    # Check if there is a missing positive number in the range 1 to max_value
    for i in range(1, max_value + 1):
        if i not in numbers:
            return "The first missing positive number is: " + str(i)

    # If all numbers from 1 to max_value in (numbers) return max_value + 1
    return "The first missing positive number is: " + str(max_value + 1)