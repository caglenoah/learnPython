def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    vowels_count = 0
    unique_vowels = set()
    for char in text:
        if char in vowels:
            vowels_count += 1
            unique_vowels.add(char)
    return vowels_count, unique_vowels