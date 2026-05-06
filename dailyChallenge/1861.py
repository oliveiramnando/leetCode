class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        def fall(box):
            ROWS, COLS = len(box), len(box[0])

            for r in range(ROWS):
                empty = COLS - 1

                for c in range(COLS - 1, -1, -1):
                    if box[r][c] == '*':
                        empty = c - 1

                    elif box[r][c] == '#':
                        box[r][c] = '.'
                        box[r][empty] = '#'
                        empty -= 1

            return box

        def rotate(box):
            ROWS, COLS = len(box), len(box[0])
            res = []

            for c in range(COLS):
                newRow = []
                for r in range(ROWS - 1, -1, -1):
                    newRow.append(box[r][c])
                res.append(newRow)

            return res

        boxGrid = fall(boxGrid)
        return rotate(boxGrid)
