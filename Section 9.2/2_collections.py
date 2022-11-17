collection = eval(input())

match collection:
    case list():
        print(collection[-1])
    case set():
        print(len(collection))
    case tuple():
        print(collection[0])