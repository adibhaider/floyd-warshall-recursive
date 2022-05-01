# Floyd-Warshall Recursive
A Python module for the recursive implementation of the Floyd-Warshall algorithm.
## What's Included
The package includes two functions: `shortest_path` and `solve_paths`. The former takes in a distance matrix, a pair of coordinates, and the number of intermediary nodes to return the shortest path for *one* pair.
```python
    def shortest_path(i, j, k, w):
      if k == 0:
        if i == j:
          return 0
        return w[i][j]
      return min(shortest_path(i, j, k - 1, w), shortest_path(i, k, k - 1, w) + shortest_path(k, j, k - 1, w))
```
The first function takes in a distance matrix and returns the shortest paths for all pairs (see example below).
```python
    def solve_paths(graph):
        for start, end, interim in product(range(len(graph)), repeat=3):
            graph[start][end] = shortest_path(start, end, interim, graph) # Calls "shortest_path"
        return graph
```
## Input and Output
```python
    # Sample input
    test = [[0, 5, no_path, 10],
            [no_path, 0, 3, no_path],
            [no_path, no_path, 0, 1],
            [no_path, no_path, no_path, 0]]
    
    # Solution
    solve_paths(test) # [[0, 5, 8, 9], [999, 0, 3, 4], [999, 999, 0, 1], [999, 999, 999, 0]]     
```
