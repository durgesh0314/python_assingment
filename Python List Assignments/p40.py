numbers = [10, 20, 30]
print("Initial list:", numbers)

numbers.append(40)
print("append(40):", numbers)

numbers.extend([50, 60])
print("extend([50, 60]):", numbers)

numbers.insert(1, 15)
print("insert(1, 15):", numbers)

numbers.remove(15)
print("remove(15):", numbers)

popped = numbers.pop()
print(f"pop(): {popped}, list: {numbers}")

print("index(30):", numbers.index(30))
print("count(20):", numbers.count(20))

numbers.sort(reverse=True)
print("sort(reverse=True):", numbers)

numbers.reverse()
print("reverse():", numbers)

copied = numbers.copy()
print("copy():", copied)

numbers.clear()
print("clear():", numbers)
