from collections import deque

def oranges_rotting(grid):

    queue = deque()

    fresh = 0

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == 2:
                queue.append([row,col])

            elif grid[row][col] == 1:
                fresh += 1


    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    minutes = 0

    while queue and fresh > 0:

        size = len(queue)

        for _ in range(size):

            row, col = queue.popleft()

            for dr, dc in directions:

                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row,new_col))

        minutes += 1

    if fresh > 0:
        return -1
    else: 
        return minutes

grid = [[2, 1, 1],[1, 1, 0],[0, 1, 1]]
result = oranges_rotting(grid)
print(result)