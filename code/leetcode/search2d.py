"""Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    l = 0
    r = (len(matrix) * len(matrix[0])) - 1
    columSize = len(matrix[0]) 
    rowSize = len(matrix[0]) 
    while l <= r:
        m = int((r + l) / 2)

        colum = int(m / columSize)
        row = int(m % rowSize)
        print(l, "---", r, "---- ", m)
        print(colum, "---", row)
        element = matrix[colum][row]
        if element < target:
            l = m + 1
        elif element > target:
            r = m - 1
        elif element == target:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 20
print(searchMatrix(matrix, target))
x = 8
rowSize = int(x/len(matrix[0]))
print("int(x/len(matrix[0])) ", int(x/len(matrix[0])))
columSize=  int(x%len(matrix[0])) 
print(matrix[rowSize][columSize])
print("stop")
