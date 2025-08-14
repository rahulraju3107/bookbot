from stats import get_number_of_words, get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = get_number_of_words(book_contents)
    num_chars = get_character_count(book_contents)
    
    print(f"{num_words} words found in the document")
    print(num_chars)

if __name__ == "__main__":
    main()