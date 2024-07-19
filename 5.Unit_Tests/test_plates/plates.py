def main():
    plate = input("Enter vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return check_length(s) and check_start_letters(s) and check_characters(s) and check_numbers(s)

def check_length(s):
    return 2 <= len(s) <= 6

def check_start_letters(s):
    return s[:2].isalpha()

def check_characters(s):
    return s.isalnum()

def check_numbers(s):
    number_already = False
    for char in s:
        if char.isdigit():
            if char == '0' and not number_already:
                return False  # No leading zero in numbers
            number_already  = True
        elif number_already:
            return False  # Letters found after numbers
    return True

main()

