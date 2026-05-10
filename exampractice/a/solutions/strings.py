word = input("Enter a word: ")

vowels = 0
consonants = 0

for i in range(len(word)):
    letter = word[i]

    # [if letter in "aeiou"]
    # this is functional, and would work, but don't do this in the exam
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)