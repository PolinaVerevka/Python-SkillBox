from collections import Counter

def can_form_palindrome(word):
    counter = Counter(word)

    odd_count = 0
    for count in counter.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    else:
        return True

def build_palindrome(word):
    counter = Counter(word)

    left_half = []
    right_half = []

    for char, count in counter.items():
        half_count = count // 2
        left_half.extend([char] * half_count)
        right_half.extend([char] * half_count)

    if any(count % 2 != 0 for count in counter.values()):
        odd_char = next(char for char, count in counter.items() if count % 2 != 0)
        left_half.append(odd_char)

    left_half.extend(reversed(right_half))

    palindrome = "".join(left_half)

    return palindrome

# Пример использования:
word = "abbcccdddd"

if can_form_palindrome(word):
    palindrome = build_palindrome(word)
    print(palindrome)
else:
    print("Невозможно составить палиндром")
