# 18. Find the Frequency of Each Character
# Write a program to count the frequency of each character in a string.
string = "hello world"
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
 
