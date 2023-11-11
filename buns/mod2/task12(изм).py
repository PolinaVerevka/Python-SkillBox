phone_number = input()

def clean_phone_number(phone_number):
    allowed_chars = "+1234567890"
    result = ""
    for char in phone_number:
        if char in allowed_chars:
            result += char
    return result

print(cleaned_number)
