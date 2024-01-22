class OthelloAI(object):
    def __init__(self, face, name):
        self.face = face
        self.name = name

    def __repr__(self):
        return f"{self.face}{self.name}"

    def move(self, board: np.array, color: int)->tuple[int, int]:
        """
        ボードの状態と色(color)が与えられたとき、
        どこに置くか返す(row, col)
        """
        valid_moves = get_valid_moves(board, color)
        return valid_moves[0]

    def say(self, board: np.array, piece: int)->str:
        if count_board(board, piece) >= count_board(board, -piece):
            return 'やったー'
        else:
            return 'がーん'

import sys

def display_board2(board, marks):
    """
    オセロ盤を表示する
    """
    global BLACK_NAME, WHITE_NAME
    clear_output(wait=True)
    for row, rows in enumerate(board):
        for col, piece in enumerate(rows):
            if (row, col) in marks:
                print(marks[(row,col)], end='')
            else:
                print(stone(piece), end='')
        if row == 1:
            print(f'  {BLACK_NAME}')
        elif row == 2:
            print(f'   {stone(BLACK)}: {count_board(board, BLACK):2d}')
        elif row == 3:
            print(f'  {WHITE_NAME}')
        elif row == 4:
            print(f'   {stone(WHITE)}: {count_board(board, WHITE):2d}')
        else:
            print()  # New line after each row

class You(OthelloAI):

    def move(self, board, color: int)->tuple[int, int]:
        """
        ボードの状態と色(color)が与えられたとき、
        どこに置くか人間に尋ねる(row, col)
        """
        valid_moves = get_valid_moves(board, color)
        MARK = '①②③④⑤⑥⑦⑧⑨'
        marks={}
        for i, rowcol in enumerate(valid_moves):
            if i < len(MARK):
                marks[rowcol] = MARK[i]
                marks[i+1] = rowcol
        display_board2(board, marks)
        n = int(input('どこにおきますか？ '))
        return marks[n]

import random

class CornerAI(OthelloAI):

    def __init__(self, face, name):
        self.face = face
        self.name = name

    def move(self, board, color: int) -> tuple[int, int]:
        """
        ボードが与えられたとき、どこに置くか(row,col)を返す
        """
        valid_moves = get_valid_moves(board, color)
        if len(valid_moves) > 0:
            corner_moves = [(0, 0), (0, 7), (7, 0), (7, 7)]
            for move in valid_moves:
                if move in corner_moves:
                    return move
        return random.choice(valid_moves)
