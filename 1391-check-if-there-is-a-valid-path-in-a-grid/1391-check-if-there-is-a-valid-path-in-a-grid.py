class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        return self.traverse(0,  0, grid)
    def traverse(self, i, j, grid):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return True
        path = False
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        store = grid[i][j]
        grid[i][j] = -69
        for direction in range(4):
            new_i = i + x[direction]
            new_j = j + y[direction]
            if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and grid[new_i][new_j] != -69:
                if self.check(i, j, store, new_i, new_j, grid):
                    path = path or self.traverse(new_i, new_j, grid)
        grid[i][j] = store
        return path
    def check(self, i, j, store, new_i, new_j, grid):
        new_store = grid[new_i][new_j]
        direction = "$"
        if new_i == i + 1:
            direction = "down"
        elif new_i == i - 1:
            direction = "up"
        elif new_j == j + 1:
            direction = "right"
        else:
            direction = "left"
         
        if direction == "up":
            if store == 2 or store == 5 or store == 6:
                if  new_store == 3 or new_store == 4 or new_store == 2:
                    return True
            return False
        if direction == "down":
            if store == 2 or store == 3 or store == 4:
                if  new_store == 5 or new_store == 6 or new_store == 2:
                    return True
            return False
        if direction == "right":
            if store == 1 or store == 4 or store == 6:
                if  new_store == 1 or new_store == 3 or new_store == 5:
                    return True
            return False
        if direction == "left":
            if store == 1 or store == 3 or store == 5:
                if  new_store == 1 or new_store == 4 or new_store == 6:
                    return True
            return False
        return False