def reverse_string(string):
    return string[::-1]

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Example usage:
my_string = "Hello, World!"

# Reverse the string
reversed_string = reverse_string(my_string)
print("Reversed string:", reversed_string)

# Count vowels in the string
vowel_count = count_vowels(my_string)
print("Number of vowels:", vowel_count)