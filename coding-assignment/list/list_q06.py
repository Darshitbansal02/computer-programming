# 6. Merge Two Lists and Remove Duplicates
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged_list = list1 + list2  # Merge the lists
merged_list = list(set(merged_list))  # Remove duplicates using set
print(merged_list)  # Output: [1, 2, 3, 4, 5]
