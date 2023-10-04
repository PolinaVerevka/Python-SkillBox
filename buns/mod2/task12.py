phone_number = input()

cleaned_number = ""
for char in phone_number:
    if char.isdigit() or char == "+":
        cleaned_number += char

print(cleaned_number)
