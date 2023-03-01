def password_validation(current_password):
    pass_is_valid = True

    if len(current_password) < 6 or len(current_password) > 10:
        print("Password must be between 6 and 10 characters")
        pass_is_valid = False

    if not current_password.isalnum():
        print("Password must consist only of letters and digits")
        pass_is_valid = False

    digit_counter = 0

    for character in current_password:
        if character.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False

    return pass_is_valid


password = input()

password_is_valid = password_validation(password)

if password_is_valid:
    print("Password is valid")
