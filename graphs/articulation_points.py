# Finding Articulation Points in Undirected Graph


"""
定义关节点的概念：如果在一个连通图中，去掉某一个顶点和从这个顶点引出的所有边之后，剩下的其他节点不在同一个连通分量里，则称这个节点为关节点。

"""


def computeAP(l):
    n = len(l)
    outEdgeCount = 0
    low = [0] * n
    visited = [False] * n
    isArt = [False] * n

    def dfs(root, at, parent, outEdgeCount):
        if parent == root:
            outEdgeCount += 1
        visited[at] = True
        low[at] = at
        # 遍历所有跟i相连接的点,to
        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                outEdgeCount = dfs(root, to, at, outEdgeCount)
                low[at] = min(low[at], low[to])  # low[at] 表示跟他相连的那些节点里面,能访问到的index最低的点.

                # AP found via bridge
                if (
                    at < low[to]
                ):  # 这就表明,我现在的点这个坐标,比到的这个点的low值还小.如果删除了at点,那么low节点就没法访问到at了.所以就断开了.所以下行赋值正确!
                    isArt[at] = True
                # AP found via cycle
                if at == low[to]:  # 如果== ,也同样道理.
                    isArt[at] = True
            else:  # 如果to 访问过.那么直接更新low[at].不用dps跑to了.只更新at节点即可.就是下行.
                low[at] = min(low[at], to)
        return outEdgeCount

    for i in range(n):
        if not visited[i]:
            outEdgeCount = 0  # parent就是父节点.因为是图,所以没有这个父节点,所以直接设置为-1即可.
            outEdgeCount = dfs(i, i, -1, outEdgeCount)
            isArt[i] = outEdgeCount > 1

    for x in range(len(isArt)):
        if isArt[x] == True:
            print(x)


# Adjacency list of graph
l = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}
computeAP(l)
