'''
The most commonly used Connect Four board size is 7 columns × 6 rows
(https://www.wikiwand.com/en/Connect_Four)
'''

def find_winner(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0:
                continue
            color = board[i][j]
            # check row
            if j+3<len(board[i]): # otherwise, there is no enough space righter to the piece for 4 pieces
                if board[i][j]==board[i][j+1]==board[i][j+2]==board[i][j+3]: #==color:
                    return color
            # check column
            if i+3<len(board): # otherwise, there is no enough space down to the piece for 4 pieces
                if board[i][j]==board[i+1][j]==board[i+2][j]==board[i+3][j]: #==color:
                    return color
            # check diag
            if i+3<len(board) and j+3<len(board[i]):
                if board[i][j]==board[i+1][j+1]==board[i+2][j+2]==board[i+3][j+3]: #==color:
                    return color
    return 0

if __name__ == '__main__':
    if 1==1==2:
        print(1)
    pass
    board = [[1,2,0,0],[2,2,0,0]]
    print(find_winner(board=board))