# Time Complexity : O(m*n), where m is the number of rows and n is the number
# of columns of the board
# Space Complexity : O(m*n)
from collections import deque

class Solution:
    def updateBoard(self, board, click):
        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),  # Upper-Left, Up, Upper-Right
            (0, -1),           (0, 1),   # Left, Right
            (1, -1),  (1, 0),  (1, 1)    # Bottom-Left, Bottom, Bottom-Right
        ]
        
        row, col = click

        # If a mine is clicked, game over
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        # BFS initialization
        queue = deque([(row, col)])

        while queue:
            r, c = queue.popleft()
            mine_count = 0

            # Count mines in adjacent cells
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == 'M':
                        mine_count += 1

            if mine_count > 0:
                # If there are adjacent mines, mark the cell with the number of
                # mines
                board[r][c] = str(mine_count)
            else:
                # If no adjacent mines, mark as 'B' and add all adjacent 'E'
                # cells to the queue
                board[r][c] = 'B'
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'E':
                        board[nr][nc] = 'B'  # Mark as visited
                        queue.append((nr, nc))

        return board

# Example 1
board1 = [['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']]
click1 = [3, 0]
print(Solution().updateBoard(board1, click1))
# Expected Output:
# [
#     ['B', '1', 'E', '1', 'B'],
#     ['B', '1', 'M', '1', 'B'],
#     ['B', '1', '1', '1', 'B'],
#     ['B', 'B', 'B', 'B', 'B']
# ]

# Example 2
board2 = [['B', '1', 'E', '1', 'B'],
    ['B', '1', 'M', '1', 'B'],
    ['B', '1', '1', '1', 'B'],
    ['B', 'B', 'B', 'B', 'B']]
click2 = [1, 2]
print(Solution().updateBoard(board2, click2))
# Expected Output:
# [
#     ['B', '1', 'E', '1', 'B'],
#     ['B', '1', 'X', '1', 'B'],
#     ['B', '1', '1', '1', 'B'],
#     ['B', 'B', 'B', 'B', 'B']
# ]

# Example 3
board3 = [['E', 'E', 'E', 'E'],
    ['E', 'M', 'M', 'E'],
    ['E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E']]
click3 = [1, 1]
print(Solution().updateBoard(board3, click3))
# Expected Output:
# [
#     ['E', 'E', 'E', 'E'],
#     ['E', 'X', 'M', 'E'],
#     ['E', 'E', 'E', 'E'],
#     ['E', 'E', 'E', 'E']
# ]