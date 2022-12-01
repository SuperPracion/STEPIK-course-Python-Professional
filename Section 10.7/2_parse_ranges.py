def parse_ranges(sting):
    for line in sting.split(','):
        start, end = map(int, line.split('-'))
        yield from range(start, end + 1)

print(*parse_ranges('7-32'))