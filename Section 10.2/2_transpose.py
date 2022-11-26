def transpose(matrix):
    return list(map(list, zip(*matrix)))

matrix = [['1', '2'],
          ['4', '5'],
          ['7', '8'],
          ['3', 4],
          [True, None],
          [9, 80],
          [1, -1]]

print(transpose(matrix))