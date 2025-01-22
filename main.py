def main():
    word_counter = 0
    letter_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_counter = len(words)
        letters = list(file_contents.lower())
        for letter in letters:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    print(f"{word_counter} words found in the document.")
    


main()
