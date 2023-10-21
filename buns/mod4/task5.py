def letter_frequency(filename):
    char_count = {}
    with open(filename, "r") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    if char.lower() in char_count:
                        char_count[char.lower()] += 1
                    else:
                        char_count[char.lower()] = 1

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1])

    with open("result.txt", "w") as file:
        for char, count in sorted_char_count:
            file.write(f"{char}: {count}\n")

letter_frequency("input.txt")
