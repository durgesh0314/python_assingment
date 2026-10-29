numbers = [10, 20, 20, 30, 40, 40, 50, 10, 60, 70]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)
