import sys

in_strings = list(sys.stdin)
news, category = sorted(in_strings[:-1]), in_strings[-1]
sorted_news = {}

for line in news:
    text, text_category, reliability = [line.strip() for line in line.split('/')]
    if text_category == category:
        sorted_news[text] = reliability

print(dict(sorted(sorted_news.items(), key=lambda x: x[1])).keys(), sep='\n')

