 # while len(lstnum)>0:
    #     for x in lstnum:
    #         i,j = x[0],x[1] 
    #         for item in board[i][j]:
    #             if item in col[j] or item in sqr[(i//3)*3+j//3]:
    #                 board[i][j].remove(item)
    #         if len(board[i][j])==1:
    #             board[i][j] = board[i][j][0]
    #             col[j][i] = board[i][j][0]
    #             sqr[(i//3)*3+j//3][(i%3)*3+j%3] = board[i][j][0]
    #             lstnum.remove((i,j))
    #         print(lstnum)