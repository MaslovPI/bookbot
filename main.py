from stats import get_num_characters, get_num_words, sort_characters
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path + "...")
    print("----------- Word Count ----------")
    text = get_book_text(path)
    print("Found " + str(get_num_words(text)) + " total words")
    print("--------- Character Count -------")
    characters = get_num_characters(text)
    sorted_characters = sort_characters(characters)
    print_char_dictionary(sorted_characters)
    print("============= END ===============")


def print_char_dictionary(characters):
    for item in characters:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))


main()
