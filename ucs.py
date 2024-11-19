
graph = {
    "S": {"A": 2, "B": 3},
    "A": {"C": 4, "D": 2},
    "B": {"D": 1, "E": 5},
    "C": {"G1": 3},
    "D": {"G2": 6, "G3": 7},
    "E": {"G3": 4},
    "G1": {},
    "G2": {},
    "G3": {}
}

start_node = "S"
goal_nodes = ["G1", "G2", "G3"]

def ucs(graph, start_node, goal_nodes):

    pq = [(0, [start_node])] 
    visited = set()
    paths = [] 

    while pq:
        pq.sort(key=lambda x: x[0]) 
        cost, path = pq.pop(0)
        current_node = path[-1]

        if current_node in goal_nodes and current_node not in visited:
            paths.append((cost, path))
            visited.add(current_node)

            if len(visited) == len(goal_nodes):
                break

        for neighbor, edge_cost in graph.get(current_node, {}).items():
                new_path = list(path)
                new_path.append(neighbor)
                pq.append((cost + edge_cost, new_path))  

    return paths

result = ucs(graph, start_node, goal_nodes)
print("All Paths to Goal Nodes with Costs:")
for cost, path in result:
    print(f"Path: {' -> '.join(path)}, Cost: {cost}")
