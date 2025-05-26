import sys
from stats import count_book_text_count, char_count_dict, sort_char_list_count
if(len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>", sys.argv)
    sys.exit(1)
def main(argv):
    path = argv[1]
    num_words = count_book_text_count(path)
    char_count = sort_char_list_count(char_count_dict(path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_count:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")
main(sys.argv)
