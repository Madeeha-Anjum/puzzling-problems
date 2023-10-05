"""
Tree
"""
from typing import Optional


class Node:
    """Definition for a Node"""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"Node {str(self.val)}, {str(self.neighbors)}"


class Solution:
    """Solution"""

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Clone Gra
        """
        for n in node:
            print(f"{n.val}, {list(map(lambda neighbor: neighbor.val, n.neighbors))}")

        #  we want to clone the graph
        # so lets get a list of neighbors list
        adjacency_list = {}
        queue = [node[0]]
        visited = []

        #  while there is something on the queue
        while queue:
            curr_node = queue.pop(0)
            visited.append(curr_node.val)

            if not curr_node.neighbors:
                continue

            neighbors = []
            for nei in curr_node.neighbors:
                if nei.val not in visited:
                    queue.append(nei)

                neighbors.append(nei.val)

            adjacency_list[curr_node.val - 1] = neighbors

        adjacency_list = dict(sorted(adjacency_list.items()))

        return self.create_graph(adjacency_list.values())

    def create_graph(self, adjacent):
        """Create a graph using adjacent matrix
        val is the 1 for index 0 ect..
        """
        graph: list[Node] = []

        # create all the nodes first
        for i in range(len(adjacent)):
            graph.append(Node(i + 1, None))

        #  assign the neighbors to the nodes
        for index, nei_list in enumerate(adjacent):
            curr_node = graph[index]
            for curr_nei in nei_list:
                get_node = graph[curr_nei - 1]
                curr_node.neighbors.append(get_node)

        return graph


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    my_graph = Solution().create_graph(adjacent=adjList)
    gr = Solution().cloneGraph(my_graph)
    print("answer")
    for n in gr:
        print(f"{n.val}, {list(map(lambda neighbor: neighbor.val, n.neighbors))}")
