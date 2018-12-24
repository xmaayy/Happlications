from requests.auth import HTTPBasicAuth
import pandas as pd
import requests
import operator
import getpass
import json
import pdb
import re

username = None
passwd = None


def auth():
    global username
    global passwd
    username = input("Please enter your github username: ")
    passwd = getpass.getpass("Password for {}:".format(username))


def strip_url(urlstr: str) -> str:
    """
    Given a url uses regex to extract the github username

    """
    if type(urlstr) is not str:
        return None
    expr = r"github\.com\/([\d\w-]*)(\/|)"
    match = re.search(expr, urlstr)
    if not match:
        # We have an error here, valid string with no github name
        # IDK what to do, but for now I'm returning None
        return None
    return match.group(1)


def languages(repos: list) -> list:
    """
    Given a users repository list, find their language rankings and
    diversity based on the repository size and the language its written in

    return list - List of tuples of lanuage and total size in ascending order
    """
    if repos == []:
        return ([None]), ([None])

    langs = {}
    for repo in repos:
        if langs.get(repo["language"]):
            langs[repo["language"]] += repo["size"]
        else:
            langs[repo["language"]] = repo["size"]
    langs = sorted(langs.items(), key=operator.itemgetter(1))
    return list(zip(*langs))


def stars(repos: list):
    """
    Give this the list of repos and a mode and it will return you the
    three metrics as a lis [min avg max total]
    """
    if repos == []:
        return [0, 0, 0, 0]
    stars = [repo["stargazers_count"] for repo in repos]
    return [min(stars), sum(stars) / len(stars), max(stars), sum(stars)]


def get_nf(repos: list):
    """
    Given all the giithub JSON data, find the non forked repositories
    and return them
    """
    non_forked = [repo for repo in repos if not repo["fork"]]
    return non_forked


def get_hub(user: str):
    """
    Get all the github JSON data for a user
    """
    if user is None:
        return []
    if username is None or passwd is None:
        auth()
    r = requests.get(
        "https://api.github.com/users/" + user + "/repos",
        auth=HTTPBasicAuth(username, passwd),
    )

    if r.status_code == 404:
        return []

    data = json.loads(r.text or r.content)
    if type(data) == dict and data.get("message") == "Bad credentials":
        print("Bad Credentials for github API")
        auth()
        return get_hub(user)

    return data


def sort_by_language(df: pd.DataFrame):
    pass


def main():
    """
    Not proper testing practices but realistically I dont have time
    to do that here. This runs a mock ranking for my personal github
    """
    data = get_hub("xmaayy")
    unique = get_nf(data)
    # I forked polybar just to test this, so you shouldnt see it pop up
    # in the next print statement
    for repo in unique:
        print(repo["name"])
    langs, sizes = languages(unique)


if __name__ == "__main__":
    main()
