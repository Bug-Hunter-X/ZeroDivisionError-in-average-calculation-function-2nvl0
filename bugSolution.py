def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#This version explicitly checks for an empty list before performing the calculation. If the list is empty, it returns 0.  Otherwise, it calculates the average as before.