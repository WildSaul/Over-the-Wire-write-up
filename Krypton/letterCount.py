from collections import Counter

def count_letter_frequencies(filename):

  letter_count = Counter()
  try:
    with open(filename, 'r') as f:
      for line in f:
        letter_count.update(char.lower() for char in line if char.isalpha())
  except FileNotFoundError:
    print(f"Error: File {filename} not found.")
    return None

  # Xếp các từ theo tần suất giảm dần
  sorted_frequencies = letter_count.most_common()
  return sorted_frequencies

# found là file tổng hợp của 3 file found1, found2, found3
filename = "found"

letter_frequencies = count_letter_frequencies(filename)

if letter_frequencies:
  for letter, count in letter_frequencies:
    print(f"Frequency of '{letter}': {count}")
