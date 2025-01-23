file = "books/frankenstein.txt"

def main():
    print(read_file())
    print(f"--- Begin report of {file} ---")
    print(f"This text has: {count_words()} words")
    for let in (sort_letter(count_letters())):
            print(f"the '{let[0]}' character was found {let[1]} times")
    print("--- End report ---")
    

def read_file(): #reads the file and puts it into a string
    with open(file) as f:
        return f.read()

def count_words(): #counts how many words are in the provided text
    words = read_file().split()
    return len(words)
    
def count_letters(): #counts how often each letter appears in the text and puts it in a dictionary
    letter_dict = {}
    text = read_file()
    letters = list(text.lower())
    for letter in letters:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict
    
def sort_letter(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return sorted_data

main()
