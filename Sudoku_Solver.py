import numpy as np


grid =[
[2, 0, 5, 0, 0, 0, 0, 0, 0],
[3, 0, 8, 6, 0, 0, 9, 0, 0],
[0, 0, 0, 1, 0, 0, 4, 0, 0],
[0, 0, 0, 0, 5, 0, 0, 1, 0],
[0, 0, 0, 0, 9, 0, 0, 2, 0],
[8, 7, 0, 0, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 8, 9, 0, 0, 3],
[0, 0, 6, 0, 0, 3, 0, 0, 5],
[5, 0, 4, 0, 0, 0, 0, 0, 1]
]


def can_insert(y,x,n):
    x0=((x)//3)*3
    y0=((y)//3)*3
    for i in range(3):
        for j in range(3):
            if(grid[y0+i][x0+j]==n):
                return False
    for i in range(9):
        if ((grid[y][i] == n) or (grid[i][x] == n)):
            return False
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if(grid[i][j]==0):
                for n in range (1,10):
                    if(can_insert(i,j,n)):
                        grid[i][j] =n
                        solve()
                        grid[i][j] =0
                return
               
    print(np.matrix(grid))
    input("more?")


solve()