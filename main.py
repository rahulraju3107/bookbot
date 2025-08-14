def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()

    return contents #string

def main():
    print(get_book_text("books/frankenstein.txt"))

if __name__ == "__main__":
    main()