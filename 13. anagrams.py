def is_anagram(str1, str2):

  if len(str1) != len(str2):
    return False

  char_count = {}
  for char in str1:
    char_count[char] = char_count.get(char, 0) + 1

  for char in str2:
    if char not in char_count or char_count[char] == 0:
      return False
    char_count[char] -= 1

  return True
  
  
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")