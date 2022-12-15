import re
import sys

text = sys.stdin.read()

text = re.sub(r'""".+?"""\n *', '', text, flags=re.MULTILINE|re.DOTALL)
text = re.sub(r'(^#.*\n|^ *#.*\n)', '', text, flags=re.MULTILINE)
text = re.sub(r' +#.*', '', text, flags=re.MULTILINE)


print(text)