def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found")
    print_report(count_letters(text))
    print(f"--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    dict_chars = {}
    for char in text.lower():
        if char.isalpha(): 
            dict_chars[char] = dict_chars.get(char, 0) + 1
    return dict_chars


def sort_on(letter_dict):
    return list(letter_dict.values())[0]


def print_report(count_dict):
    list_of_dict = [{entry: count_dict[entry]} for entry in count_dict]
    list_of_dict.sort(reverse=True, key=sort_on)
    for letter_dict in list_of_dict:
        for key, value in letter_dict.items():
            print(f"The letter '{key}' appeared {value} times")


if __name__ == '__main__':
    main()
