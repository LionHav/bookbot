from stats import get_num_char, get_num_words, get_sorted_dict
import sys

def main():
    ##book_path = "books/frankenstein.txt"
    if len(sys.argv)==2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(book_path)
    words = get_num_words(text)
    dict=get_num_char(text)
    #print(f"{words} words found in the document")
    #print(dict)
    list_of_dict=get_sorted_dict(dict)
    print_report(list_of_dict,book_path,words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(list_dict,path,word_count):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in list_dict:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")




main()