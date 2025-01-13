def read_book():
  with open("./books/frankenstein.txt") as f:
    return f.read()

def word_count(text):
  text = read_book()
  words = text.split()
  return words.count

def main():
  print(word_count(read_book()))

if __name__ == "__main__":
  main()
