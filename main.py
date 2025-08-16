from stats import get_number_of_words, get_character_count, sorted_list

# Reads and returns contents of text file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    book = "books/frankenstein.txt"
    book_contents = get_book_text(book)

    # Get stats
    num_words = get_number_of_words(book_contents)
    num_chars = get_character_count(book_contents)
    sorted_chars = sorted_list(num_chars)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()