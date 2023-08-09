# Get User Input
old_text = input("Enter the text\n")
amount_shift = int(input("Enter the amount to shift\n"))

# Available characters
characters = ["a", "b", "c", "d",
              "e", "f", "g", "h",
              "i", "j", "k", "l",
              "m", "n", "o", "p",
              "q", "r", "s", "t",
              "u", "v", "w", "x",
              "y", "z"]


def cipher(old_text):
    new_text = ""

    for letter in old_text:
        if letter.islower():

            new_text += characters[check_index(letter)]

        elif letter.isupper():

            # Keeping Capitalization of input text
            new_text += characters[check_index(letter)].upper()

    # Handle whitespace
        else:
            new_text += letter

    return new_text


# Find Index of original text and new text
def check_index(letter):
    original_index = characters.index(letter.lower())

    # Continue over lenght of characters to find matching character
    if (original_index + amount_shift > len(characters)):
        return (original_index + amount_shift) % len(characters)
    else:
        return original_index + amount_shift


def main():
    print(cipher(old_text))


if __name__ == "__main__":
    main()
