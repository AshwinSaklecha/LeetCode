class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        sorted_queries = []
        for i in range(len(queries)):
            sorted_queries.append((i, queries[i]))
        def query_sort(y):
            return y[1]
        sorted_queries.sort(key=query_sort)

        def log_sort(y):
            return y[1]
        logs.sort(key=log_sort)

        # everything sorted 
        ans = [0] * len(queries)
        my_dict = {}
        i, j = 0, 0
        for query in sorted_queries :
            start = query[1] - x
            end = query[1]
            while j < len(logs) and logs[j][1] <= end :
                server = logs[j][0]
                if server in my_dict :
                    my_dict[server] += 1
                else :
                    my_dict[server] = 1
                j += 1
            while i < len(logs) and logs[i][1] < start :
                server = logs[i][0]
                if server in my_dict:
                    my_dict[server] -= 1
                    if my_dict[server] == 0 :
                        my_dict.pop(server)
                i += 1
            
            idx = query[0]
            ans[idx] = n - len(my_dict)

        return ans