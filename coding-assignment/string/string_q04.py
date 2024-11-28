# 4. Reverse Each Word in a String
# Write a program to reverse each word in a sentence while keeping the word order intact.
input_string = "hello world"
reversed_words = ""
words = input_string.split()
for word in words:
    reversed_words += word[::-1] + " "
print(reversed_words.strip())  # Output: "olleh dlrow"
