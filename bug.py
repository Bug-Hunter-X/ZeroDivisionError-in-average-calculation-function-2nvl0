def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#The bug is that it does not handle the case of an empty list correctly.  It should return 0 or raise an exception instead of causing a ZeroDivisionError.