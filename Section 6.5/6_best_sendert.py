from collections import *

def best_sender(messages, senders):
    result = defaultdict(int)

    for sender in range(len(senders)):
        result[senders[sender]] += len(messages[sender].split())

    return max(result, key=lambda x: (result[x], x)) #sorted by value -> else name
