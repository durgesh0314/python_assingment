numbers = [45, 12, 89, 89, 23, 7, 65]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print("List:", numbers)
print("Second largest number:", second_largest)
