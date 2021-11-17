# match_words
lookup words in the grid of characters

- pre_process:
Lookups words with lengths of between 3 and 10 and saves as dictionary.json file.

- checkMatch:
finds the first character of the word in the grid and recursively calls the matching method to travel according to each character of the word.

# Test
> python3 -m unittest discover
# Run
> python3 app.py
