class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        my_set = set()
        for i in range(len(grid)):
            first_server = None
            for j in range(len(grid[i])):
                if grid[i][j] == 1 :
                    if first_server == None :
                        first_server = (i, j)
                    else :
                        if first_server not in my_set:
                            my_set.add(first_server)
                        my_set.add((i, j))
        for j in range(len(grid[0])):
            first_server = None 
            for i in range(len(grid)):
                if grid[i][j] == 1 :
                    if first_server == None :
                        first_server = (i, j)
                    else :
                        if first_server not in my_set:
                            my_set.add(first_server)
                        my_set.add((i, j))
        return len(my_set)