#!/usr/bin/python3


def parse_input(lines):
    calls = [int(call) for call in lines.pop(0).split(",")]

    boards = []
    board = []
    for line in lines:
        row = [int(cell) for cell in line.split()]
        if len(row) == 5:
            board.append(row)
            if len(board) == 5:
                boards.append(board)
                board = []

    return (boards, calls)


def mark(board, call):
    for r, row in enumerate(board):
        board[r] = ["x" if cell == call else cell for cell in row]


def has_won(board):
    for i in range(5):
        if all([board[i][j] == "x" for j in range(5)]):
            return True
        if all([board[j][i] == "x" for j in range(5)]):
            return True
    return False


def find_first_winning_board(boards, calls):
    for call in calls:
        for board in boards:
            mark(board, call)
            if has_won(board):
                return (board, call)


def find_last_winning_board(boards, calls):
    one_remaining = False
    for call in calls:
        for board in boards:
            mark(board, call)
        if one_remaining:
            if has_won(boards[0]):
                return (boards[0], call)
        else:
            boards = [board for board in boards if not has_won(board)]
            if len(boards) == 1:
                one_remaining = True
                


def score(board, call):
    return call * sum([sum([cell for cell in row if cell != "x"]) for row in board])


with open('4.txt') as input:
    (boards, calls) = parse_input(input.readlines())

    (board, call) = find_last_winning_board(boards, calls)

    print(score(board, call))
