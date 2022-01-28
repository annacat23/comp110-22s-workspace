"""Ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730310234"

five_letter_word: str = str(input("Enter a 5-character word: "))

if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:

    single_character: str = str(input("Enter a single character: "))
    count: int = 0

    if len(single_character) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:

        print("Searching for " + single_character + " in " + five_letter_word)

        if single_character == (five_letter_word)[0]:
            print(single_character + " found at index 0 ")
            count = count + 1

        if single_character == (five_letter_word)[1]:
            print(single_character + " found at index 1 ")
            count = count + 1

        if single_character == (five_letter_word)[2]:
            print(single_character + " found at index 2 ")
            count = count + 1

        if single_character == (five_letter_word)[3]:
            print(single_character + " found at index 3 ")
            count = count + 1

        if single_character == (five_letter_word)[4]:
            print(single_character + " found at index 4 ")
            count = count + 1

        if count == 0:
            print("No instances of " + single_character + " found in " + five_letter_word)
        else:
            if count == 1:
                print("1 instance of " + single_character + " found in " + five_letter_word)
            else:
                print(count, "instances of " + single_character + " found in " + five_letter_word)