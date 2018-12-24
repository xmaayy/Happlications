import github
from github import *


class TestClass:
    def teardown_method(self, method):
        """
        The easiest way to get pytest not to flip out
        when the user is prompted. Somehow I dont need to
        do this for getpass
        """
        github.input = input

    def test_strings(self):
        """
        Test the regex, I dont know how good this coverage is
        but its good enough for me
        """
        inputs = [
            "https://github.com/xmaayy",
            "https://github.com/user1",
            "",
            "hello",
        ]
        outputs = ["xmaayy", "user1", None, None]
        github.input = lambda x: "xmaayy"
        for ind, inp in enumerate(inputs):
            out = strip_url(inp)
            assert out == outputs[ind]

    def test_empty(self):
        """
        Test an empty github account. This was the first one
        I found
        """
        github.input = lambda x: "xmaayy"
        data = get_hub("javapiston14")
        assert data == []

    def test_full(self):
        """
        Test all the data from a github account, with permission from
        me  :)
        """
        github.input = lambda x: "xmaayy"
        data = get_hub("xmaayy")
        assert data != []
        print(data[1].keys())
        repolist = [repo["name"] for repo in data]
        assert repolist == [
            "Alexandria",
            "cipher",
            "CUHackAPIO",
            "DarkBot",
            "megacrypt.js",
            "MGAN",
            "NoFace",
            "polybar",
            "SFMLinstall",
            "SubHelper",
            "UpStat",
            "Website",
            "xmaayy.github.io",
        ]
