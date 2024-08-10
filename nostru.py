adj = [[1, 2], [0, 2], [0, 1]]  # Adjacency list representation of a graph
src = 0  # Starting node

for i in range(len(adj[src])):
    print(f"Index: {i}, Adjacent Node: {adj[src][i]}")
