n = int(input("Enter number of elements: "))
user_list = []
for i in range(n):
    val = input(f"Enter element {i + 1}: ")
    user_list.append(val)
print("User created list:", user_list)
