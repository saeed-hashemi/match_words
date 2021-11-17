import pandas as pd


def pre_process(regex):
    """
    reads data from dict.json and apply filter by regex 
    and saves selected values as dictionary.json file

    Parameters
    --------------------
    regex: str -> contains regex string

    Returns
    --------------------
    None
    """
    sr = pd.read_json("data/dict.json", typ='series')
    sr = sr[sr.str.match(regex)]
    sr.to_json("data/dictionary.json", orient='values')
