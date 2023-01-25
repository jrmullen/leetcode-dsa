class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = collections.defaultdict(set)
        columnset = collections.defaultdict(set)
        squareset = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                element = board[i][j]
                if element == '.':
                    continue

                square = (i // 3, j // 3) # integer division rounds down, e.g. coordinates [1, 7] -> [1/3, 7/3] -> square [0, 3]

                if element in rowset[i] or element in columnset[j] or element in squareset[square]:
                    return False

                rowset[i].add(element)
                columnset[j].add(element)
                squareset[(i // 3, j // 3)].add(element)

        return True
