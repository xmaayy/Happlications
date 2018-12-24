# Happlications
A small console application to help with sorting through applicants. It allows for grouping by different categories, as well as performs basic ranking of github and text based answers

# How to use it
The data you're sorting should be in the same directory as `ranking.py`, I may change it so that you can type in a different path but for now it is what it is.

Its going to ask you for your github credentials first. This is used to grab github data for each of the participants that provided their link, I couldnt use unauthenticated github api requests because that maxes at 60/hr, and I'm not put
ting any kind of hardcoded key or password in here.

```
Please enter your github username: xmaayy
Password for xmaayy:
  2%|█▌                                                                            | 11/566 [00:02<02:04,  4.45it/s]
```

once its fetched all that data youll be prompted for what to do

```
What would you like to do? (sort, export, exit): 
```

From here on out the prompts should be enough to guide you. Make sure to use the export function once you've done all your sorting to actually save the results. The filename should be `<filename>.csv` when you input it, and you'll find it in the same folder that the original data was in.

# The Data it works with
Data should be raw exported CSV's from typeform. There are two hardcoded columns in the code, but theyre in the ranking.py file and its used for making data more uniform, and for table formatting. Feel free to delete the lines that deal with that and it will have no effect on the code.
