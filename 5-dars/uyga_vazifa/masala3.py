def func(matrix: list, coordinate: str) -> str:
    ustun = ord(coordinate[0]) - 65
    satr = int(coordinate[1]) - 1

    if matrix[ustun][satr] == '.':
        return "splash"
    return "BOOM"

lst = [
    ['.', '.', '.', '*', '*'],
    ['.', '*', '.', '.', '.'],
    ['.', '*', '.', '.', '.'],
    ['.', '*', '.', '.', '.'],
    ['.', '.', '*', '*', '.'],
]

koord = "A4"
print(func(lst, koord))