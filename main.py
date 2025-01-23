def main():
    print(read_file())
    print(f"This text has: {count_words()} words")
    

def read_file(): #reads books/frankenstein.txt and puts it into a string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(): #counts how many words are in the provided text
    word_counter = 0
    words = read_file().split()
    word_counter = len(words)
    return word_counter
    
def count_letters(): #counts how often each letter appears in the text and puts it in a dictionary
    letter_dict = {}
    text = read_file()
    letters = list(text.lower())
    for letter in letters:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict
    


main()
