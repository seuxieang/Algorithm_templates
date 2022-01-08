from collections import defaultdict, deque


# dfs
def findOrderDFS(num: int, prerequisites):
        edges = defaultdict(list)   # 存储有向图
        visited = [0] * num     # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        result = list()     # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        valid = True    # 判断有向图中是否有环
        for info in prerequisites:
            edges[info[1]].append(info[0])
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1  # 将节点标记为「搜索中」
            # 搜索其相邻节点,只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2      # 将节点标记为「已完成」
            result.append(u)        # 将节点入栈
        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(num):
            if valid and not visited[i]:
                dfs(i)
        if not valid:
            return list()
        # 如果没有环，那么就有拓扑排序,注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]

# bfs

def findOrderBFS(num: int, prerequisites):
    edges = defaultdict(list)   # 存储有向图
    indeg = [0] * num   # 存储每个节点的入度
    result = list()     # 存储答案
    for info in prerequisites:
        edges[info[1]].append(info[0])
        indeg[info[0]] += 1
    q = deque([u for u in range(num) if indeg[u] == 0])     # 将所有入度为 0 的节点放入队列中
    while q:
        u = q.popleft()     # 从队首取出一个节点
        result.append(u)    # 放入答案中
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:    # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                q.append(v)
    if len(result) != num:
        result = list()
    return result

if __name__ == '__main__':
    # print(findOrderBFS(4,[[1,0],[2,0],[3,1],[3,2]]))
    print(findOrderDFS(4,[[1,0],[2,0],[3,1],[3,2]]))