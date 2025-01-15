def main():
  book_path = "books/frankenstein.txt"
  generate_report(book_path)

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
  
def generate_report(book_path):
  path = book_path
  print(f"### Word and Character count report on file {path} ###")
  text = get_book_text(path)
  word_count = get_num_words(text)
  char_count = get_character_count(text)
  print(f"{word_count} words found in the document.")
  print("# List of characters and ocurrances in the document.")
  for key,value in char_count.items():
    print(f"- The character \"{key}\" has {value} ocurrances.")

main()
