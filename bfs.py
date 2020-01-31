
def BFS(graph: dict, s: str):
    # graph 无向图
    # s 开始的节点
    # 一层一层走，每次只找相邻的节点
    queue = [s]
    seen = [s]
    path = []
    parent = {s: None}
    while queue:
        node = queue.pop(0)
        nodes = graph[node]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.append(w)
                parent[w] = node
        path.append(node)
    return path, parent

def DFS(graph: dict, s: str):
    # graph 无向图
    # s 开始的节点
    # 一条道找到黑
    stack = [s]
    seen = [s]
    path = []
    
    while stack:
        node = stack.pop()
        nodes = graph[node]
        for w in nodes:
            if w not in seen:
                # 加入到stack和seen中
                stack.append(w)
                seen.append(w)
        path.append(node)
    return path

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "C", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
        }
    path, parent = BFS(graph, "E")

    v = 'A'
    while v != None:
        print(v)
        v = parent[v]
