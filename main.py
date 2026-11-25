
print("Welcome to Password Strength Checker")

password = input("Enter your password: ")

score = 0
suggestions = []

# Check password length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1
else:
    suggestions.append("Add an uppercase letter")

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1
else:
    suggestions.append("Add a lowercase letter")

# Check numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    suggestions.append("Add a number")

# Check special characters
if any(char in "!@#$%^&*()-_+=?" for char in password):
    score += 1
else:
    suggestions.append("Add a special character")

# Display score
print("\nPassword Score:", score, "/ 5")

# Display strength
if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

# Display suggestions
if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Your password satisfies all five rules!")


