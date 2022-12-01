def nonempty_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_lines = (line for line in file)
        non_empty = (line for line in file_lines if not line.isspace())
        non_new_line = (line.rstrip() for line in non_empty)
        lines = (line if len(line) < 25 else '...' for line in non_new_line)

        yield from lines