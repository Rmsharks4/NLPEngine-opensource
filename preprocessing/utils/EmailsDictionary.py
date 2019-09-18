import re


class EmailsDictionary:

    standard_re = None
    semi_standard_re = None
    non_standard_re = None
    replace_text = None

    @staticmethod
    def load():
        EmailsDictionary.standard_re = re.compile(r'\w*@\w*\.\w*')
        EmailsDictionary.semi_standard_re = re.compile(r'\w*\.\w*')
        EmailsDictionary.non_standard_re = re.compile(r'\w*\sdot\s\w*')
        EmailsDictionary.replace_text = '$EMAIL'
