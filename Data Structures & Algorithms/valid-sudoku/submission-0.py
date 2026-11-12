class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def populateAndCheck(grid, n) -> bool:

            for i in range(len(grid)):
                for j in range(len(grid[i])):

                    if grid[i][j] == ".":
                        grid[i][j] = str(n)
                        n += 1
                    elif grid[i][j] != "." and int(grid[i][j]) > 9:
                        return False

            return True

        
        populateNcheck = populateAndCheck(board, n=10)
        if not populateNcheck:
            return False

        #rule 1 check
        for eachList in board:

            if len(set(eachList)) != len(eachList):
                return False

        #rule 2 check
        for i in range(9):
            st = set()
            for j in range(len(board)):
                st.add(board[j][i])
            if len(st) != len(board):
                return False

        #rule 3 checker
        row,column=0,0
        while row+3 < 9:

            while column+3 < 9:

                lst = board[row][column : column+3] + board[row+1][column : column+3] + board[row+2][column : column+3]

                if len(set(lst)) != len(lst):
                    return False

                column += 3

            column = 0
            row += 3

        return True





        



        