class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for num in row:
                if num in seen:
                    return False
                elif num == ".":
                    continue
                seen.add(num)

        for column in range(9):
            seen = set()
            for row in range(9):
                num = board[row][column]
                if num in seen:
                    return False
                elif num  == ".":
                    continue
                seen.add(num)
            
        for minBoard in range(9):
            seen = set()
            startRow = (minBoard // 3) * 3
            startCol = (minBoard % 3) * 3
            for numI in range(3):
                for numJ in range(3):
                    numero = board[numI + startRow][numJ + startCol]
                    if numero == ".":
                        continue
                    elif numero in seen:
                        return False
                    seen.add(numero)

                    
        return True 


            
        
                
                
                
                
        
        
        