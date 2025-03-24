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
      
def sorted_char_count(char_count):
  ordered_char_count = {k: char_count[k] for k in sorted(char_count.keys())}
  for key,value in ordered_char_count.items():
    if key.isalpha():
      print(f"{key}: {value}")
  