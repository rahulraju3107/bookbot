def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def get_number_of_words(contents):
    return len(contents.split())

def main():
    num_words = get_number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()