# 19. Find the Difference Between Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
diff = list(set(list1) - set(list2))
print(diff)  # Output: [1, 2]
