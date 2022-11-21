def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {k + 1: v for k, v in enumerate(matrix)}

annotations = matrix_to_dict.__annotations__

print(annotations['return'])