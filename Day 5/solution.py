import collections

def solve_one(rows) -> int:

    # Filter out any rows that don't have "|" in them
    req_numbers_list: list = [row.strip() for row in rows if "|" in row and row.strip()]

    def ordering(req_numbers: list) -> list:
        priority_graph: collections.defaultdict[str, list] = collections.defaultdict(list)
        priority_degree: collections.defaultdict[str, int] = collections.defaultdict(int)
        sorting: collections.deque = collections.deque()
        nodes: set = set()

        # Build graph and in-degrees
        for line in req_numbers:
            x, y = line.strip().replace(" ", "").split("|")
            priority_graph[x].append(y)
            priority_degree[y] += 1
            nodes.add(x)
            nodes.add(y)

        # Ensure that all nodes appear in priority_degree
        for node in nodes:
            if node not in priority_degree:
                priority_degree[node] = 0

        # Start with nodes having zero in-degree
        filtered_nodes = [node for node in nodes if priority_degree[node] == 0]
        sorting.extend(filtered_nodes)

        priority_queue: list = []

        while sorting:
            current_node = sorting.popleft()
            priority_queue.append(current_node)

            for next_node in priority_graph[current_node]:
                priority_degree[next_node] -= 1
                if priority_degree[next_node] == 0:
                    sorting.append(next_node)

        # Check for cycles
        if len(priority_queue) != len(nodes):
            raise ValueError("Cycle detected in the dependency rules.")

        return priority_queue

    sorted_nodes = ordering(req_numbers_list)
    ##print("Topologically sorted order:", sorted_nodes)
    return len(sorted_nodes)


if __name__ == "__main__":

    with open("input.txt") as f:
        req_numbers = f.readlines()

        try:
            print(solve_one(req_numbers))
        except ValueError as e:
            print(e)
