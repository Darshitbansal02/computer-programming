# 2. Find the Common Elements in Two Lists
list1 = [1, 2, 3]
list2 = [2, 3, 4]
common_elements = list(set(list1) & set(list2))  # Using set intersection
print(common_elements)  # Output: [2, 3]
