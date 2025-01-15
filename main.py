def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  char_count =  get_character_count(text)
  print(f"{num_words} words found in the document")
  print(f"{char_count}")

def get_num_words(text):
  words = text.split()
  return len(words)

def get_character_count(text):
  char_count = {}
  lowercase_string = text.lower()
  
  for char in lowercase_string:
    if char.isalpha():
      char_count[char] = char_count.get(char, 0) + 1
  
  return char_count
    

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()
