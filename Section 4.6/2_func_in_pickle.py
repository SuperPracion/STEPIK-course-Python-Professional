import pickle
import sys

funk = pickle.load(open(input(), 'rb'))
words = [word.strip() for word in sys.stdin]

print(words)
print(funk)