# 14. Write a function that finds the longest word in a list of strings.

def longest_word(words):
    return max(words, key=len)

# Example usage
print(longest_word(["apple", "banana", "cherry"]))  # Output: "banana"
