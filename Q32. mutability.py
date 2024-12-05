# Define a list of numbers
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Modify an element by index
numbers[2] = 35
print("After modifying the third element:", numbers)

# Append a new element to the list
numbers.append(60)
print("After appending 60:", numbers)

# Insert an element at a specific position
numbers.insert(1, 15)
print("After inserting 15 at index 1:", numbers)

# Remove an element by value
numbers.remove(40)
print("After removing 40:", numbers)

# Remove an element by index using pop()
removed_item = numbers.pop(3)
print(f"After popping the element at index 3 ({removed_item}):", numbers)

# Extend the list with another list
numbers.extend([70, 80, 90])
print("After extending with [70, 80, 90]:", numbers)

# Sort the list in ascending order
numbers.sort()
print("After sorting in ascending order:", numbers)

# Reverse the list
numbers.reverse()
print("After reversing the list:", numbers)
