from collections import *

def wins(pairs):
    results = defaultdict(set)

    for winner, looser in pairs:
        results[winner].add(looser)

    return results
