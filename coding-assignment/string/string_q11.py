# 11. Count the Number of Words in a String
# Write a program to count the number of words in a given string.
string = "Hello world, how are you?"
word_count = 0
for word in string.split():
    word_count += 1
print("Word count:", word_count)  # Output: 5
