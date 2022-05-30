import os
import random
board_matrix = []
board_column = []
a = 5
b = 5


def ship(c):
    board_line = []
    for i in range(a):
        board_line.append("-")
    if c == 0:
        board_line.pop(c)
        board_line.insert(c, "=")
        board_line.pop(c+1)
        board_line.insert(c+1, ">")
    elif c == a-1:
        board_line.pop(c)
        board_line.insert(c, "=")
        board_line.pop(c-1)
        board_line.insert(c-1, ">")
    else:
        board_line.pop(c)
        board_line.insert(c, "=")
        board_line.pop(c-1)
        board_line.insert(c-1, "<")
        board_line.pop(c+1)
        board_line.insert(c+1, ">")
    board_matrix.insert(2*b+1, board_line)
    board_matrix.pop(2*b)


def create_X():
    board_line = []
    for i in range(b):
        for i in range(a):
            board_line.append("X")
        board_matrix.append(board_line)
        board_line = []


def create_blank():
    board_line = []
    for i in range(b):
        for i in range(a):
            board_line.append(" ")
        board_matrix.append(board_line)
        board_line = []


def create_board():
    c = int(a/2)
    for i in range(a):
        board_column.append(b-1)
    create_X()
    create_blank()
    board_matrix.append([])
    ship(c)


def show_matrix():
    c = 2*b + 1
    for i in range(c):
        line = board_matrix[i]
        str_line = ""
        for j in range(a):
            str_line = str_line + line[j]
        print(str_line)


def round(indeks):
    ship(indeks)
    line_number = int(board_column[indeks])
    line = board_matrix[line_number]
    line.pop(indeks)
    line.insert(indeks, " ")
    board_matrix.pop(line_number)
    board_matrix.insert(line_number, line)
    if board_column[indeks] >= 0:
        x = board_column[indeks] - 1
        board_column.pop(indeks)
        board_column.insert(indeks, x)


def check():
    for i in range(a):
        c = 2*b - 1
        if board_column[i] == c:
            print("przegrałeś")
            exit()


def add():
    for i in range(a):
        x = int(board_column[i]) + 1
        board_column.pop(i)
        board_column.insert(i, x)
    for i in range(a):
        line_number = int(board_column[i])
        line = board_matrix[line_number]
        line.pop(i)
        line.insert(i, "X")
        board_matrix.pop(line_number)
        board_matrix.insert(line_number, line)


def clear_window():
    os.system('cls')
    print()


create_board()

# instrukcja

end = True
while end:
    add_or_not = random.randint(0, 3)
    clear_window()
    show_matrix()
    indeks = input()
    try:
        int(indeks)
    except ValueError:
        "zły indeks"
    else:
        indeks = int(indeks) - 1
        if indeks < a:
            round(indeks)
            if add_or_not == 0:
                add()
            check()
            print(board_column)
        else:
            print("zła koluna")
