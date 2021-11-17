import pandas as pd
from utils.data_manipulation import pre_process
from utils.process import checkMatch
from utils.user_input import input_matrix


if __name__ == "__main__":

    # read the words with defined regex and save as dictionary.json file
    pre_process("[a-z]{3,10}$")

    # load dictionary
    dictionary = pd.read_json("data/dictionary.json", typ='series')

    # read grid of chracters from input
    while True:
        grid = input_matrix()
        if isinstance(grid, list):
            break
        else:
            print(grid)

    results = []
    # seeking for matching words (if a word exist in the grid add it to results)
    for i in range(dictionary.size):
        if (checkMatch(grid, dictionary[i])):
            results.append(dictionary[i])
    print(results)
