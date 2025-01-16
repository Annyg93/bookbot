def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letter_count_dict = counting_letters(text)
    print(letter_count_dict)
    display_report(num_words ,letter_count_dict)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def counting_letters(text):
    letter_count = {}
    words = text.lower()

    for letter in words:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count


def display_report(num_words, letter_count_dict):
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    chars_list = []
    for char, count in letter_count_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]
    chars_list.sort(reverse=True, key=sort_on)

    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

    








main()

