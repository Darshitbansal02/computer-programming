# 13. Find the Longest Word in a String
# Write a program to find the longest word in a sentence.
input_string = "The quick brown fox jumps over the lazy dog"
words = input_string.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)  # Output: "jumps"
