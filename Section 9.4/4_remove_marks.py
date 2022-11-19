def remove_marks(text, marks):
    remove_marks.count += 1

    return ''.join(filter(lambda symbol: symbol not in marks, text))

remove_marks.__dict__.setdefault('count', 0)

text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)