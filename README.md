# Floyd-Warshall Recursive
A Python module for the recursive implementation of the Floyd-Warshall algorithm.
## What's Included
The package includes two functions: `shortest_path` and `solve_paths`. The former takes two coordinates and a distance matrix to return the shortest path for *one* pair.
```python
    def shortest_path(i, j, w):
      k = 3
      if k == 0:
        if i == j:
          return 0
        return w[i][j]
      return min(shortest_path(i, j, k - 1, w), shortest_path(i, k, k - 1, w) + shortest_path(k, j, k - 1, w))
```
The second function takes in a distance matrix and returns the shortest paths for all pairs.
```python
    def solve_paths(graph):
        for start, end, interim in product(range(len(graph)), repeat=3):
            graph[start][end] = shortest_path(start, end, interim, graph) # Calls "shortest_path"
        return graph
```
## Input and Output
**Note:** The `no_path` variable has been explicitly declared as `999` in the following example.
```python
    # Sample input
    test = [[0, 5, no_path, 10],
            [no_path, 0, 3, no_path],
            [no_path, no_path, 0, 1],
            [no_path, no_path, no_path, 0]]
    
    # Solution
    solve_paths(test) # [[0, 5, 8, 9], [999, 0, 3, 4], [999, 999, 0, 1], [999, 999, 999, 0]]     
```
## How to Implement
Copy the `floyd.py` module into the code directory and import `solve_paths` and `no_path` from it.
## Testing
The `tests.py` file contains three test cases for unit testing. More test cases may be added by including additional methods inside the `Test` class.
## License
Please see https://github.com/adibhaider/floyd-warshall-recursive/blob/main/LICENSE.
