import sys
from stats import get_book_wordcount, char_count, sort_char_freq
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1] 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    # return contents of book file
    book_text = get_book_text(path_to_book)
    # print wordcount of book contents to console
    print(f"Found {get_book_wordcount(book_text)} total words")
    print("--------- Character Count -------")
    character_freq = char_count(book_text)
    # print(character_freq)
    sorted_list = (sort_char_freq(character_freq))
    # if the characters is not alphabetical don't print it.
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()