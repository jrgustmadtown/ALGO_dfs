import sys

input = sys.stdin().readline().splitlines()
t = int(input[0])
index = 1
graphs = []

for _ in range(t):
    n = int(input[index])
    index += 1
    names = []
    adjacency = [[] for _ in range(n)]  # [[], [], ...] n times
    lines = input[index:index + n]  # ["A B", "B A C", ...]
    index += n

    # node names - O(n)
    for line in lines:
        dissect = line.split()  # "A B" → ["A", "B"]
        name = dissect[0]
        names.append(name)

    # make adjacency list - O(m) (O(n*m) but n <= 100)
    for i, line in enumerate(lines):
        dissect = line.split()
        for adj in dissect[1:]:
            j = names.index[adj]
            adjacency[i].append(j)

    # depth first search - O(n+m) - O(n) for node, seperate O(m) for edge
    visited = n*[False]
    output = []

    def dfs(node):
        visited[node] = True
        output.append(names[node])
        for node_ in adjacency[node]:
            if not visited[node_]:
                dfs[node_]

    dfs(0)
    print(" ".join(output))

