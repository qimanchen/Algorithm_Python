import heapq
import math

def init_distance(graph: dict, s: str) -> dict:
    """
    初始化其他节点的距离为正无穷
    防止后面字典越界
    """
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph: dict, s: str):
    # graph 无向图
    # s 开始的节点
    # 一层一层走，每次只找相邻的节点
    pqueue = []
    # 将第一个节点初始化，并压入到优先队列中
    # 以第一个节点为根节点, 记录的优先级为对应的
    # 从某个节点到s节点的距离

    # 注意优先队列中，对应的优先级在前
    heapq.heappush(pqueue,(0,s))

    # 已处理的节点
    seen = []

    # 用于存储对应已处理节点的前一个节点
    parent = {s: None}
    
    distance = init_distance(graph, s)
    while pqueue:
        dist, node = heapq.heappop(pqueue)

        # 得到对应已处理节点的相邻节点
        nodes = graph[node].keys()
        seen.append(node)
        
        for w in nodes:
            if w not in seen:
                 # 如果对应的节点距离小于distance
                if dist + graph[node][w] < distance[w]:
                    heapq.heappush(pqueue, (dist+graph[node][w], w))
                    
                    # 同时更新对应的父系数组
                    parent[w] = node
                    # 并更新相应w节点到s节点的最短距离
                    distance[w] = dist + graph[node][w]
    return parent, distance

def get_path(parent, node):
    """
    通过父系列表得到对应的node 到 s的path
    """
    path = []
    while node != None:
        path.append(node)
        node = parent[node]
    return path[::-1]


if __name__ == "__main__":
    graph = {
        "A": {"B":5, "C":1},
        "B": {"A":5, "C":2, "D":1},
        "C": {"A":1, "B":2, "D":4, "E":8},
        "D": {"B":1, "C":4, "E":3, "F":6},
        "E": {"C":8, "D":3},
        "F": {"D":6}
        }
    s = "A"
    parent, distance = dijkstra(graph, s)
    
    print(get_path(parent, "D"))
