
# Case Study 29: Password Policy Validation Engine

print("========================================")
print("       PASSWORD POLICY VALIDATION")
print("========================================")

# Password policy rules
minimum_length = 8

prohibited_words = ["password", "admin", "123"]

# Number of passwords to check
n = int(input("Enter number of sample passwords: "))

if n <= 0:
    print("Invalid number of passwords!")

else:

    for i in range(n):

        print("\nPassword", i + 1)

        password = input("Enter a sample password: ")

        errors = []

        # Check minimum length
        if len(password) < minimum_length:
            errors.append("Password must contain at least 8 characters.")

        # Character category checking
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for ch in password:

            if ch >= 'A' and ch <= 'Z':
                has_upper = True

            elif ch >= 'a' and ch <= 'z':
                has_lower = True

            elif ch >= '0' and ch <= '9':
                has_digit = True

            else:
                has_special = True

        if not has_upper:
            errors.append("Missing uppercase letter.")

        if not has_lower:
            errors.append("Missing lowercase letter.")

        if not has_digit:
            errors.append("Missing digit.")

        if not has_special:
            errors.append("Missing special character.")

        # Check repeated consecutive characters
        repeated = False

        for j in range(len(password) - 2):

            if (password[j] == password[j + 1] and
                password[j] == password[j + 2]):

                repeated = True
                break

        if repeated:
            errors.append("Three or more consecutive identical characters are not allowed.")

        # Check prohibited words
        lower_password = password.lower()

        for word in prohibited_words:

            if word in lower_password:
                errors.append("Contains prohibited text: " + word)

        # Display results
        print("\nValidation Result:")

        if len(errors) == 0:

            print("Password is VALID.")
            print("All password rules are satisfied.")

        else:

            print("Password is INVALID.")
            print("Failed Conditions:")

            for error in errors:
                print("-", error)

    print("\n========================================")
    print("       VALIDATION COMPLETED")
    print("========================================")
