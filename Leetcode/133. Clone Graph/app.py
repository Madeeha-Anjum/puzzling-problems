from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({str(self.val)}, {str(self.neighbors)})"


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        if len(node.neighbors) == 0:
            return Node(node.val, None)

        # deep_copied_neighbors = [self.cloneGraph()]

        adjacency_values = {}

        explored_values = []
        nodes_queue = [node]

        while len(nodes_queue) != 0:
            # keep exploring and updating the adjacency list
            curr_node = nodes_queue.pop(0)

            if curr_node.val in explored_values:
                continue

            explored_values.append(curr_node.val)

            nodes_queue.extend(curr_node.neighbors)

            curr_node_index = curr_node.val

            adjacency_values[curr_node_index] = list(
                map(lambda n: n.val, curr_node.neighbors)
            )

        sorted_tuples = dict(sorted(adjacency_values.items()))

        return create_graph(list(sorted_tuples.values()))


def create_graph(values: list[list[int]]):
    graph = []

    for i in range(len(values)):
        graph.append(Node(i + 1, None))

    for index, neighbor_values in enumerate(values):
        node = graph[index]
        for neighbor_value in neighbor_values:
            neighbor_node_index = neighbor_value - 1
            neighbor_node = graph[neighbor_node_index]
            node.neighbors.append(neighbor_node)

    return graph[0]
    # for node in graph:
    #     print(f"{node.val}, {list(map(lambda n: n.val, node.neighbors))}")


def main():
    # create_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    Solution().cloneGraph(create_graph([[2, 4], [1, 3], [2, 4], [1, 3]]))


main()
