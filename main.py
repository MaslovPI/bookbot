from stats import get_num_words, get_num_characters

def get_book_text(path_to_file):
        with open (path_to_file) as f:
            file_content = f.read()
            return file_content

def main():
    text = get_book_text("books/frankenstein.txt")
    print("Found "+str(get_num_words(text)) +" total words")
    print(get_num_characters(text))

main()
