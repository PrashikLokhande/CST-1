def reverse_string(word):
  reversed_word = ""
  for letter in word:
    reversed_word = letter + reversed_word
  return reversed_word

word = input("Enter a word: ")
reversed_word = reverse_string(word)
print("Reversed word:", reversed_word)