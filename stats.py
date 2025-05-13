def get_words_from_book(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  
  return len(file_contents.split())

def count_occurences(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  occurrences = {}
  cleaned_contents = "".join(file_contents.split()).lower()
  for character in cleaned_contents:
    if character not in occurrences:
      occurrences[character] = 1
    else:
      occurrences[character] += 1
  
  return occurrences

def sort_on(dict):
  return dict["count"]

def sort_occurences(occurrences):
  occurrences_list = []
  for c in occurrences:
    occurrences_list.append(({"name": c, "count": occurrences[c]}))
  occurrences_list.sort(reverse=True, key=sort_on)
  return occurrences_list
