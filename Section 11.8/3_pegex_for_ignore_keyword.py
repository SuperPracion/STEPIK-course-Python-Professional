import re
import keyword


def search_word_in_keywords(match_obj):
    if match_obj.group().lower() in map(str.lower, keyword.kwlist):
        return '<kw>'
    return match_obj.group()


print(re.sub(r'\b\w+\b', search_word_in_keywords, input()))
