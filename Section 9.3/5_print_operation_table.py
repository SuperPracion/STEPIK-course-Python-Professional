def print_operation_table(operation, row, cols):
    for i in range(row):
        for j in range(cols):
            print(str(operation(i+1, j+1)).ljust(3), end=' ')
        print()
