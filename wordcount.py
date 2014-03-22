#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###


def create_dict(filename):
  "gets items from file and returns dictionary with words and their frequency"
  f = open(filename, 'rU')
  text = f.read()
  text = text.lower()
  text_arr = text.split()
  words_dict = { }
  for w in text_arr:
    if w in words_dict:
      words_dict[w] = words_dict[w] + 1
    else:
      words_dict[w] = 1
  f.close()
  return words_dict


def print_words(filename):
  "prints words from file in abc order and shows how often this word apperars in file"  
  words_dict = create_dict(filename)
  for w in sorted(words_dict.keys()):
    print w, words_dict[w]
  #sys.exit(1)


def get_sorting_item(items):
  "sorting method - first item in tuple"
  return items[1]



def print_top(filename):
  "prints top 20 most frequent words"
  words_dict = create_dict(filename)
  words_list = sorted(words_dict.items(), key=get_sorting_item, reverse=True)
  for word in words_list[:20]:
    print word[0], word[1]


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
