# 18. Find the Frequency of Each Character
# Write a program to count the frequency of each character in a string.
input_string = "hello world"
freq = {}
for char in input_string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)  # Output: {'h':
