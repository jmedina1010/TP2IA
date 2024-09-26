def exhaustive_search(start, goal, choices, path=[]):
    path = path + [start]
    if start == goal:
        return path
    if start not in choices:
        return None
    for node in choices[start]:
        if node not in path:
            newpath = exhaustive_search(node, goal, choices, path)
            if newpath:
                return newpath
    return None

def heuristic(a, b):
    # Simple heuristic example: straight-line distance
    return abs(ord(a) - ord(b))

def a_star_search(start, goal, choices):
    import heapq
    
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), start))
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in choices.get(current, []):
            tentative_g_score = g_score[current] + 1  # assuming uniform cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

# Example usage
choices = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': ['T']
}

result_exhaustive = exhaustive_search('A', 'T', choices)
print("Path found (Exhaustive):", result_exhaustive)

result_a_star = a_star_search('A', 'T', choices)
print("Path found (Heuristic):", result_a_star)