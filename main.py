from stats import get_num_words
from stats import get_character_count
from stats import sorted_char_count
import sys

def get_book_text(path):
  with open(path, "r") as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python main.py <path>")
    sys.exit(1)

  path = sys.argv[1]
  text = get_book_text(path)
  num_words = get_num_words(text)
  char_count = get_character_count(text)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words.")
  print("--------- Character Count --------")
  sorted_char_count(char_count)

main()