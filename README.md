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

# Columns

0. \#
1. First Name:
2. Last Name:
3. Nice to meet you {{answer_102301024}}, what email can we reach you with?
4. In case of an emergency at the event, what is your cell number?
5. Will you be 18 or older by February 16th, 2019?
6. What do you identify as?
7. Other
8. Which race / ethnicity do you identify with?
9. What school do you attend?
10. What is the name of your school?
11. What do you study at {{answer_102301040}}?
12. What do you study at {{answer_102301026}}?
13. When do you expect to graduate?
14. How many Hackathons have you been to before?
15. Halal
16. Vegetarian
17. Lactose free
18. Peanut free
19. Tree nut free
20. Gluten free
21. Other.1
22. T-shirt sizes (Unisex):
23. Would you require travel reimbursement if available?
24. Where are you travelling from?
25. What do you want to get out of cuHacking?
26. Tell us about your favorite project you've worked on over the past year. If you haven't worked on one, tell us about one you'd want to do!
27. Resume (.pdf, .png, .docx):
28. GitHub:
29. LinkedIn:
30. Personal Website:
31. MLH Code of Conduct
32. MLH Privacy Policy
33. MLH Contest Terms<br>Please go through the Contest Terms at:
34. Is there anything you would like to tell us that we didn't ask?
35. Start Date (UTC)
36. Submit Date (UTC)
37. Network ID
38. Best Language:
39. Language Info:
40. Total Stars:
41. Star Info:

