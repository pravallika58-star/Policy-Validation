# Policy-Validation
# Case Study 29: Password Policy Validation Engine

## Python Activity-Based Learning

### Student Details
- **Name:** DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01AO383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

The Password Policy Validation Engine is a Python-based program that checks sample passwords according to predefined validation rules.

The program evaluates password length, uppercase letters, lowercase letters, digits, special characters, repeated characters and prohibited words.

It displays whether the password is valid or invalid and explains all the conditions that are not satisfied.

## 2. Objectives

- To validate sample passwords using Python.
- To check minimum password length.
- To identify uppercase and lowercase letters.
- To check the presence of digits and special characters.
- To detect repeated consecutive characters.
- To identify prohibited words or substrings.
- To display failed validation conditions.

## 3. Assumptions

1. The minimum password length is 8 characters.
2. Every password must contain at least one uppercase letter.
3. Every password must contain at least one lowercase letter.
4. Every password must contain at least one digit.
5. Every password must contain at least one special character.
6. Three or more consecutive identical characters are not allowed.
7. The prohibited substrings are `password`, `admin` and `123`.
8. Password validation is case-insensitive for prohibited substrings.
9. Only sample passwords are used for this educational program.

## 4. Algorithm

1. Start the program.
2. Set the minimum password length to 8.
3. Define the prohibited words.
4. Enter the number of sample passwords.
5. Read each sample password.
6. Check whether the password has at least 8 characters.
7. Check for uppercase and lowercase letters.
8. Check for digits and special characters.
9. Check for three or more consecutive identical characters.
10. Check for prohibited substrings.
11. Store all failed conditions in a list.
12. If no conditions fail, display Password Valid.
13. Otherwise, display Password Invalid and explain the failed conditions.
14. Repeat for all passwords.
15. Stop the program.

## 5. Pseudocode

```text
START

SET minimum_length = 8

SET prohibited_words =
    password, admin, 123

INPUT number_of_passwords

IF number_of_passwords <= 0
    DISPLAY Invalid input

ELSE

    FOR each password

        INPUT password
        INITIALIZE errors list

        IF length(password) < 8
            ADD length error
        END IF

        INITIALIZE:
            uppercase = FALSE
            lowercase = FALSE
            digit = FALSE
            special = FALSE

        FOR each character in password

            CHECK character category

        END FOR

        IF uppercase = FALSE
            ADD uppercase error
        END IF

        IF lowercase = FALSE
            ADD lowercase error
        END IF

        IF digit = FALSE
            ADD digit error
        END IF

        IF special = FALSE
            ADD special character error
        END IF

        CHECK repeated consecutive characters

        IF repeated characters found
            ADD repetition error
        END IF

        CHECK prohibited substrings

        IF errors list is empty
            DISPLAY Password Valid
        ELSE
            DISPLAY Password Invalid
            DISPLAY all failed conditions
        END IF

    END FOR

END IF

STOP
```

## 6. Python Source Code

**File name:** `password_validation.py`

The complete Python program is included in this folder.

## 7. Test Cases

| Test Case | Sample Password | Expected Result |
|---|---|---|
| 1 | Good@2026 | Valid |
| 2 | abc | Invalid |
| 3 | Pass@123 | Invalid |
| 4 | ABC@1234 | Invalid |
| 5 | Aaaa@1234 | Invalid |
| 6 | Hello@2026 | Valid |
| 7 | admin@2026 | Invalid |

## 8. Expected Output

```text
PASSWORD POLICY VALIDATION

Password 1:
Good@2026

Password is VALID.
All password rules are satisfied.

Password 2:
abc

Password is INVALID.

Failed Conditions:
- Password must contain at least 8 characters.
- Missing uppercase letter.
- Missing digit.
- Missing special character.

Password 3:
Pass@123

Password is INVALID.

Failed Conditions:
- Contains prohibited text: 123

VALIDATION COMPLETED
```

## 9. Conclusion

The Password Policy Validation Engine successfully checks sample passwords against predefined validation rules. It identifies missing character categories, insufficient length, repeated characters and prohibited substrings.

This project helps us understand Python variables, strings, conditional statements, loops, lists and string operations. It also improves logical thinking and problem-solving skills.

---

**Project:** Python Activity-Based Learning  
**Case Study Number:** 29  
**Topic:** Password Policy Validation Engine
