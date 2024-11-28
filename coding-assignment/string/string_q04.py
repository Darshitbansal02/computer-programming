# 4. Reverse Each Word in a String
# Write a program to reverse each word in a sentence while keeping the word order intact.
string = "hello world"
reversed_words = ' '.join(word[::-1] for word in string.split())
print(reversed_words)  # Output: "olleh dlrow"
