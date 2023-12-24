import numpy as np
import pandas as pd
from tqdm import tqdm
import re
import nltk
# Download the "words" identifier under "Copra" from the popup (one time thing)
# import ssl
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()

word_list = nltk.corpus.words.words()

# select only 5 letter words from the dictionary
word_len_5 = list(set([
    i.upper() for i in word_list if len(i) == 5
]))

# read known hints
hints = pd.read_csv(
    r"/Users/wrngnfreeman/Library/CloudStorage/OneDrive-Personal/Documents/Work/Personal projects/wordle/hints.csv",
    dtype={"Letter": str, "Omit": str, "True Position": str, "False Position": str}
)
hints["Omit"] = [True if str(hints.loc[i, "Omit"]).lower()=="true" else False for i in hints.index]
# list letters that are not present
letters_not_present = [
    i.upper() for i in hints["Letter"].tolist() if hints.loc[hints["Letter"]==i, "Omit"].values[0] == True
]
# list letters that are present
letters_present = [
    i.upper() for i in hints["Letter"].tolist()\
    if  (str(hints.loc[hints["Letter"]==i, "True Position"].values[0]) != "nan") |\
        (str(hints.loc[hints["Letter"]==i, "False Position"].values[0]) != "nan")
]
# create a dictionary of true and false letter positions
letter_postions = {}
for letter in letters_present:
    true_position = hints.loc[hints["Letter"] == letter, r"True Position"].values[0]
    if str(true_position) == "nan":
        true_position = [np.NaN]
    else:
        true_position = true_position.split(",")
    false_position = hints.loc[hints["Letter"] == letter, r"False Position"].values[0]
    if str(false_position) == "nan":
        false_position = [np.NaN]
    else:
        false_position = false_position.split(",")
    letter_postions = {
        **letter_postions,
        **{letter: {
            "True Position": true_position,
            "False Position": false_position
        }}
    }

# word selection by elimination
final_word_list = []
for word in tqdm(word_len_5):
    # do not consider words that contains any of the letters that are not present
    if bool(re.search(pattern="".join(["["] + letters_not_present + ["]"]), string=word.upper())):
        continue
    elif set("".join(letters_present)) <= set(word.upper()):
        # consider words that contains all of the letters that are present
        true_check = []
        for letter in letters_present:
            # check positions
            ## check true positions
            for true_pos in letter_postions[letter]["True Position"]:
                if str(true_pos) != "nan":
                    if bool(re.compile(letter).match(
                        string=word.upper(),
                        pos=int(true_pos)
                    )):
                        true_check = true_check + [True]
                    else:
                        true_check = true_check + [False]
                else:
                    pass
            ## check false positions
            for false_pos in letter_postions[letter]["False Position"]:
                if str(false_pos) != "nan":
                    if bool(re.compile(letter).match(
                        string=word.upper(),
                        pos=int(false_pos)
                    )):
                        true_check = true_check + [False]
                    else:
                        true_check = true_check + [True]
                else:
                    pass
        if False in true_check:
            continue
        else:  # select only those words where all conditions are met
            final_word_list = final_word_list + [word.upper()]
    else:
        continue

# print recommendations
print(final_word_list)
