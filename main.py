import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import get_word_count, get_character_count, get_sorted_characters

def main ():
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    char_count = get_character_count(book_text)
    sorted = get_sorted_characters(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

main()