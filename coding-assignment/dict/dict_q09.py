# 9. Nested Dictionary Update

# Problem: You want to update values in a nested dictionary and add new keys if they don’t exist.

nested_dict = {
    'user1': {'name': 'John', 'age': 25, 'location': {'city': 'New York', 'country': 'USA'}},
    'user2': {'name': 'Alice', 'age': 30, 'location': {'city': 'London', 'country': 'UK'}}
}

updates = {
    'user1': {'age': 26, 'location': {'city': 'San Francisco'}},  # Update age and city for user1
    'user3': {'name': 'Bob', 'age': 35, 'location': {'city': 'Paris', 'country': 'France'}}  # Add user3
}

result = update_nested_dict(nested_dict, updates)
print(result)

# Output:
# {
#     'user1': {'name': 'John', 'age': 26, 'location': {'city': 'San Francisco', 'country': 'USA'}},
#     'user2': {'name': 'Alice', 'age': 30, 'location': {'city': 'London', 'country': 'UK'}},
#     'user3': {'name': 'Bob', 'age': 35, 'location': {'city': 'Paris', 'country': 'France'}}
# }
 
