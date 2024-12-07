def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 30, 40, 50, 0]
average = calculate_average(my_numbers)
print(f"The average is: {average}")