def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

my_list = [5, 2, 9, 1, 7]
result = find_largest(my_list)
print("The largest number in the list is:", result)