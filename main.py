from stats import get_words_from_book, count_occurences, sort_occurences

def main():
  word_count = get_words_from_book("books/frankenstein.txt")

  word_occurences = count_occurences("books/frankenstein.txt")

  sorted_occurences = sort_occurences(word_occurences)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for c in sorted_occurences:
    if c["name"].isalpha():
      print(f"{c["name"]}: {c["count"]}")

  print("============= END ===============")

main()
