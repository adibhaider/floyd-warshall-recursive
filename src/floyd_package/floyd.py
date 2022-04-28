# Only importing the necessary functions within a module
from sys import maxsize
from itertools import product

no_path = maxsize


def shortest_path(i, j, k, w):
    """Recursive function to find the shortest path between "i" and "j" with "k" as the intermediary"""
    if k == 0:
        if i == j:
            return 0
        return w[i][j]
    # Recursive call to the function to eventually reach the base case
    return min(shortest_path(i, j, k - 1, w), shortest_path(i, k, k - 1, w) + shortest_path(k, j, k - 1, w))


def solve_paths(graph):
    """Function to replace all values within the multidimensional list "graph" with the shortest paths"""
    for start, end, interim in product(range(len(graph)), repeat=3):
        # Calls the "shortest_path" function for each combination of "start" and "end"
        graph[start][end] = shortest_path(start, end, interim, graph)
    return graph
