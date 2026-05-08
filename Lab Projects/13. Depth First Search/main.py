def dfs(adj_matrix, reference: int) -> list:
    # Check if Reference Node is within the Total Number of Nodes in the Graph
    matrix_length = len(adj_matrix)
    if not 0 <= reference < matrix_length:
        return 'Invalid Node'
    
    # Initialize DFS Stack and Set of Visited nodes
    visited = set()
    stack = [reference]

    # Iterate while Stack is not Empty
    while stack:
        # Get the element from the Stack for processing
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)

            # Iterate over ALL the Nodes as new_node for further reference
            for new_node in range(matrix_length):

                # Checks if new_node has not been visited and if an edge exists connecting it to current_node
                if new_node not in visited and adj_matrix[current_node][new_node]:
                    stack.append(new_node)

    # Returns a List of all nodes reachable from the reference node
    # 'visited' list contains all nodes reachable from reference. Type Cast to list to fit requirements of the Problem
    return list(visited)

