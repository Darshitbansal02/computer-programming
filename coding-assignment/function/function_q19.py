# 19. Define a function that checks if a given string is a valid email address by ensuring it contains both `@` and a `.` after `@`.

def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

# Example usage
print(is_valid_email("test@example.com"))  # Output: True
