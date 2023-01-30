class Sudoku:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        
    def is_valid(self):
        # check for invalid value types (boolean)
        for row in self.data:
            for val in row:
                if type(val) != int:
                    return False
        
        # check for values not in valid range 1..N
        for row in self.data:
            for val in row:
                if val < 1 or val > self.n:
                    return False
        
        # check for empty field(s)
        for row in self.data:
            for val in row:
                if val == None:
                    return False
        
        # check for 1x1 with wrong value
        if self.n == 1 and self.data[0][0] != 1:
            return False
        
        # check rows
        for row in self.data:
            if len(set(row)) != self.n:
                return False
        
        # check columns
        for i in range(self.n):
            if len(set([row[i] for row in self.data])) != self.n:
                return False
        
        # check 'little squares'
        sqrt_n = int(self.n ** 0.5)
        for i in range(0, self.n, sqrt_n):
            for j in range(0, self.n, sqrt_n):
                little_square = [self.data[x][y] for x in range(i, i + sqrt_n) for y in range(j, j + sqrt_n)]
                if len(set(little_square)) != self.n:
                    return False
        
        return True

# Valid Sudoku
goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],  
  [1]
])

#test.it('should be valid')
print(goodSudoku1.is_valid()) #, True, 'Testing valid 9x9')
print(goodSudoku2.is_valid()) #, True, 'Testing valid 4x4')

#test.it ('should be invalid')
print(badSudoku1.is_valid()) #, False, 'Values in wrong order')
print(badSudoku2.is_valid()) #, False, '4x5 (invalid dimension)')