# Floyd-Warshall Recursive
A Python module for the recursive implementation of the Floyd-Warshall algorithm.
## What's Included
The package includes two functions. The first function takes in a distance matrix and returns the (see example below).
```python
    def shortest_path(i, j, k, w):
      if k == 0:
        if i == j:
          return 0
        return w[i][j]
      return min(shortest_path(i, j, k - 1, w), shortest_path(i, k, k - 1, w) + shortest_path(k, j, k - 1, w))
```
The second function solves a distance matrix by calling the first 
```python
    def solve_paths(graph):
        for start, end, interim in product(range(len(graph)), repeat=3):
            graph[start][end] = shortest_path(start, end, interim, graph) # Calls "shortest_path"
        return graph
```
## Input
```python
