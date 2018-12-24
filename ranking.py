from metrics.generic_fns import *
from metrics.github import *
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import pdb

# The relevant columns used for prompting later
rel_cols = ["First Name:", "Last Name:"]

# Columns we need to make as uniform as possible (lowercase, remove symbols,
# remove spaces?). 
uni_cols = ["Which race / ethnicity do you identify with?"]

def rank_github(data: pd.DataFrame):
    """
    Get a relative ranking for students based on their github.
    This is based on star and unforked repo size. This also grabs a 
    users top language from their repos
    """
    rankdata = pd.DataFrame(columns=["Name", "GHuser"])
    names = [row[1][1] + row[1][2] for row in list(data.iterrows())]
    githubs = [row[1]["GitHub:"] for row in list(data.iterrows())]

    rankdata["Name"] = names
    rankdata["GHuser"] = githubs
    # pdb.set_trace()
    rankdata["GHuser"] = [
        strip_url(user) for user in rankdata["GHuser"].values
    ]

    starcount = []
    langdata = []
    top_lang = []
    all_stars = []
    _ = get_hub("xmaayy")  # Trigger the login prompt early
    for user in tqdm(rankdata["GHuser"].values):
        userdata = get_hub(user)
        if userdata is not None and userdata is not []:
            unique = get_nf(userdata)
            langs, sizes = languages(unique)
            top_lang.append(langs[-1])
            langdata.append((langs, sizes))
            starcount.append(stars(unique))
            all_stars.append(starcount[-1][-1])
        else:
            starcount.append([0, 0, 0])
            langdata.append((None, None))
    data["Best Language:"] = top_lang
    data["Language Info:"] = langdata
    data["Total Stars:"] = all_stars
    data["Star Info:"] = starcount

    return data
    

def get_wc(data: pd.DataFrame, col: int):
    """
    Get the word counts of the open answer questions
    """
    label = data.columns[col]
    answers = data[label].values
    lens = [len(answer.split()) if type(answer) is str else 0 for answer in answers ]
    data["WordCount{}".format(col)] = lens
    return data

def sort_data(data: pd.DataFrame):
    """
    This function is part of the main interactive loop of the program.
    Its used to sort the applicants based on criteria, like age, 
    # of hackathons, github ranking, etc. The sorting can be done within
    subgroups as well. So you could sort by github ranking based on number
    of hackathons done, graduation date, etc.
    """
    group_columns = []
    # This is the code responsible for grouping, has a small event loop
    # in it that breaks after a valid selection has been entered
    grby = input("Do you want to group by a column before sorting? (y/n): ")
    grby = True if grby == 'y' else False
    if grby:
        for ind, col in enumerate(data.columns):
            print("{0}. {1}".format(ind, col))
        while True:
            group = input("Please select a column to group by (# above): ")
            try:
                grcol = int(group)
                if grcol == -1: grby = False
                break
            except ValueError:
                print("Please enter the number of the desired column above")
                print("or -1 to cancel grouping")
    if grby:
        print("Grouping by {0}".format(data.columns[grcol]))
        group_columns.append(data.columns[grcol])
    
    # Sorting the dataframe
    for ind, col in enumerate(data.columns):
        print("{0}. {1}".format(ind, col))

    srt_col = input("Which column do you want to sort by?")
    try:
        srt_col = int(srt_col)
        if srt_col == -1: return data
        group_columns.append(data.columns[srt_col])
    except ValueError:
        print("Please enter the number of the desired column above")
        print("or -1 to cancel sorting")

    if grby:
        data = data.sort_values(group_columns, ascending=False)
        print(data[["First Name:"] + group_columns].head(3))
    else:
        data = data.sort_values(group_columns, ascending=False)
        print(data[["First Name:"] + group_columns].head(3))

    return data 


def export(data: pd.DataFrame):
    while True:
        try: 
            filename = input("Enter a new filename: ")
            filename = Path(filename)
            data.to_csv(filename)
            print("Saved")
            break
        except Exception as e:
            print(e)
            print("Error. Trying again")


def prompt_gen(data: pd.DataFrame):
    print(data[rel_cols].head(5))

    cmd = input("\n What would you like to do? (sort, export, exit): ")
    if cmd == 'sort':
        data = sort_data(data)
    elif cmd == 'export':
        export(data)
    elif cmd == 'exit':
        return False, data
    
    return True, data

def main():
    data = pd.read_csv("cu.csv")
    data = rank_github(data) 
    data = get_wc(data,25)
    data = get_wc(data,26)
    data[uni_cols[0]] = [re.sub(r'\W+', '', str(string)).lower() for string in data[uni_cols[0]]]
    runloop = 1
    while runloop:
        runloop, data = prompt_gen(data)
        
if __name__ == "__main__":
    main()
