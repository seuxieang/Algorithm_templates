import heapq
import math



def dijkstra(n, graph, start = 0) -> int:
    # build the undirected g
    g = [[] for _ in range(n)]
    for u, v, w in graph:
        g[u].append((v, w))
        g[v].append((u, w))

    q = [(0, start)]
    times, seen = [math.inf] * n, [0] * n
    times[start] = 0

    while q:
        time, curr = heapq.heappop(q)
        # print(f'{curr = } {time = }')
        if seen[curr]: continue
        seen[curr] = 1
        for nxt, nxt_time in g[curr]:
            if time + nxt_time < times[nxt]:
                times[nxt] = time + nxt_time
                heapq.heappush(q, (time + nxt_time, nxt))

    return times[-1]

if __name__ == '__main__':
    print(dijkstra(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                           [0, 4, 5], [4, 6, 2]]))