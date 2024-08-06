# Time Complexity : O(n^2)
# Space Complexity : O(n^2)
from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        if not board or not board[0]:
            return 0

        n = len(board)
        moves = [-1] * (n * n + 1)  # 1D representation of the board
        queue = deque([1])  # BFS queue
        moves[1] = -2  # Mark the first cell as visited
        steps = 0
        idx = 1
        left_to_right = True

        # Flatten 2D array
        for i in range(n - 1, -1, -1):
            if left_to_right:
                for j in range(n):
                    moves[idx] = board[i][j]
                    idx += 1
            else:
                for j in range(n - 1, -1, -1):
                    moves[idx] = board[i][j]
                    idx += 1
            left_to_right = not left_to_right

        # Perform BFS
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == n * n:
                    return steps
                for j in range(1, 7):
                    next_pos = curr + j
                    if next_pos <= n * n and moves[next_pos] != -2:
                        if moves[next_pos] != -1:
                            queue.append(moves[next_pos])
                        else:
                            queue.append(next_pos) # Snake or Ladder
                        moves[next_pos] = -2  # Mark as visited
            steps += 1

        return -1

# Example 1
board1 = [[-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]
print(Solution().snakesAndLadders(board1))  # Output: 4

# Example 2
board2 = [[-1, -1, -1, -1, 48, 5, -1],
    [12, 29, 13, 9, -1, 2, 32],
    [-1, -1, 21, -1, -1, -1, -1],
    [42, 37, 21, -1, -1, 26, -1],
    [28, -1, 26, 10, -1, -1, 36],
    [22, 33, 18, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1]]
print(Solution().snakesAndLadders(board2))  # Output: 5

# Example 3
board3 = [[-1, -1, -1, -1],
    [14, -1, 11, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, 15]]
print(Solution().snakesAndLadders(board3))  # Output: 2
