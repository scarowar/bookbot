import sys
from stats import get_words_from_book, count_occurences, sort_occurences

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]

  word_count = get_words_from_book(f"{book_path}")

  word_occurences = count_occurences(f"{book_path}")

  sorted_occurences = sort_occurences(word_occurences)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for c in sorted_occurences:
    if c["name"].isalpha():
      print(f"{c["name"]}: {c["count"]}")

  print("============= END ===============")

main()
