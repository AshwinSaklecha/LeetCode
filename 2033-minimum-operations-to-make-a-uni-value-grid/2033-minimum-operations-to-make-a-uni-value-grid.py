class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        is_same = True
        is_doable = True
        num_to_compare = grid[0][0]
        starting_point = grid[0][0]
        while starting_point > 0:
            starting_point -= x
        starting_point += x
        my_dict = {}
        sorted_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sorted_list.append(grid[i][j])
                if (grid[i][j] - starting_point) % x != 0:
                    is_doable = False
                if grid[i][j] != num_to_compare:
                    is_same = False
                if grid[i][j] in my_dict:
                    my_dict[grid[i][j]] += 1
                else:
                    my_dict[grid[i][j]] = 1
        if is_same :
            return 0
        if not is_doable:
            return -1
        element = -1
        sorted_list.sort()
        if len(sorted_list) % 2 != 0:
            element = sorted_list[len(sorted_list) // 2]
        else:
            contender1 = sorted_list[len(sorted_list) // 2]
            contender2 = sorted_list[(len(sorted_list) // 2) - 1]
            if my_dict[contender1] >= my_dict[contender2]:
                element = contender1
            else:
                element = contender2
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff = abs(grid[i][j] - element)
                ans += (diff // x)
        return ans