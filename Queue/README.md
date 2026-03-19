# Queue Data Structure - GeeksforGeeks Implementations

This folder contains Python implementations of Queue-based algorithms and data structures from GeeksforGeeks DSA tutorials.

## Table of Contents

| # | File | Topic | Approaches |
|---|------|-------|------------|
| 1 | [stack_using_queue.py](stack_using_queue.py) | Implement Stack using Queues | 3 |
| 2 | [queue_using_stacks.py](queue_using_stacks.py) | Implement Queue using Stacks | 3 |
| 3 | [level_order_traversal.py](level_order_traversal.py) | Level Order Traversal | 2 |
| 4 | [bfs_graph.py](bfs_graph.py) | BFS Graph Traversal | 2 |
| 5 | [fifo_page_replacement.py](fifo_page_replacement.py) | FIFO Page Replacement | 1 |
| 6 | [k_queues_array.py](k_queues_array.py) | K Queues in Array | 2 |
| 7 | [reverse_queue.py](reverse_queue.py) | Reverse Queue | 2 |
| 8 | [reverse_first_k.py](reverse_first_k.py) | Reverse First K Elements | 3 |
| 9 | [first_non_repeating.py](first_non_repeating.py) | First Non-Repeating Character | 3 |
| 10 | [knight_min_steps.py](knight_min_steps.py) | Knight Minimum Steps to Target | 1 |
| 11 | [sliding_window_maximum.py](sliding_window_maximum.py) | Sliding Window Maximum | 3 |
| 12 | [shortest_path_maze.py](shortest_path_maze.py) | Shortest Path in Maze | 2 |
| 13 | [generate_binary_numbers.py](generate_binary_numbers.py) | Generate Binary Numbers | 2 |
| 14 | [max_cost_path_k_nodes.py](max_cost_path_k_nodes.py) | Maximum Cost Path with K Nodes | 1 |
| 15 | [snake_ladder.py](snake_ladder.py) | Snake and Ladder | 2 |
| 16 | [shortest_safe_route.py](shortest_safe_route.py) | Shortest Safe Route | 2 |
| 17 | [count_paths_k_edges.py](count_paths_k_edges.py) | Count Paths with K Edges | 2 |
| 18 | [min_cost_simple_path.py](min_cost_simple_path.py) | Minimum Cost Simple Path | 1 |
| 19 | [min_cost_path_intermediates.py](min_cost_path_intermediates.py) | Minimum Cost via Intermediates | 1 |

---

## Algorithm Details

### 1. Stack using Queues
Implement a stack using queue operations.

| Approach | Time | Space |
|----------|------|-------|
| Two Queues (push O(n), pop O(1)) | O(n) push, O(1) pop | O(n) |
| Two Queues (push O(1), pop O(n)) | O(1) push, O(n) pop | O(n) |
| Single Queue (amortized) | O(1) amortized | O(n) |

### 2. Queue using Stacks
Implement a queue using stack operations.

| Approach | Time | Space |
|----------|------|-------|
| Two Stacks (enqueue O(1), dequeue O(n)) | O(1) enqueue, O(n) dequeue | O(n) |
| Two Stacks (enqueue O(n), dequeue O(1)) | O(n) enqueue, O(1) dequeue | O(n) |
| Two Stacks (amortized) | O(1) amortized | O(n) |

### 3. Level Order Traversal
Print tree nodes level by level.

| Approach | Time | Space |
|----------|------|-------|
| Recursive (queue-based) | O(n) | O(n) |
| Morris Traversal | O(n) | O(1) |

### 4. BFS Graph Traversal
Breadth-First Search traversal of a graph.

| Approach | Time | Space |
|----------|------|-------|
| Iterative (queue) | O(V+E) | O(V) |
| Recursive (with queue) | O(V+E) | O(V) |

### 5. FIFO Page Replacement
First-In-First-Out page replacement algorithm.

| Approach | Time | Space |
|----------|------|-------|
| Basic FIFO | O(pages × frames) | O(frames) |

### 6. K Queues in Array
Implement K queues in a single array.

| Approach | Time | Space |
|----------|------|-------|
| Space-efficient | O(1) enqueue/dequeue | O(n) |
| Alternative | O(1) amortized | O(n) |

### 7. Reverse Queue
Reverse a queue using recursion/stack.

| Approach | Time | Space |
|----------|------|-------|
| Stack-based | O(n) | O(n) |
| Recursive | O(n) | O(n) |

### 8. Reverse First K Elements
Reverse first K elements of a queue.

| Approach | Time | Space |
|----------|------|-------|
| Stack-based | O(n) | O(k) |
| Recursive | O(n) | O(k) |
| LinkedList-based | O(n) | O(k) |

### 9. First Non-Repeating Character
Find first non-repeating character in stream.

| Approach | Time | Space |
|----------|------|-------|
| HashMap + Queue | O(n) | O(1) |
| Array + Queue | O(n) | O(1) |
| OrderedDict | O(n) | O(1) |

### 10. Knight Minimum Steps
Find minimum steps for knight to reach target.

| Approach | Time | Space |
|----------|------|-------|
| BFS | O(n²) | O(n²) |

### 11. Sliding Window Maximum
Find maximum in each sliding window.

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n×k) | O(1) |
| Deque | O(n) | O(k) |
| PriorityQueue | O(n log k) | O(k) |

### 12. Shortest Path in Maze
Find shortest path in binary maze.

| Approach | Time | Space |
|----------|------|-------|
| BFS | O(rows×cols) | O(rows×cols) |
| BFS (optimized) | O(rows×cols) | O(rows×cols) |

### 13. Generate Binary Numbers
Generate binary numbers from 1 to N.

| Approach | Time | Space |
|----------|------|-------|
| Queue (string) | O(n) | O(n) |
| Queue (bit manipulation) | O(n) | O(n) |

### 14. Max Cost Path with K Nodes
Find maximum cost path with K nodes.

| Approach | Time | Space |
|----------|------|-------|
| DFS | O(V+E) | O(V) |

### 15. Snake and Ladder
Find minimum dice throws to reach end.

| Approach | Time | Space |
|----------|------|-------|
| BFS (graph) | O(V) | O(V) |
| BFS (optimized) | O(V) | O(V) |

### 16. Shortest Safe Route
Find shortest path avoiding danger cells.

| Approach | Time | Space |
|----------|------|-------|
| BFS with visited | O(rows×cols) | O(rows×cols) |
| BFS (safe zone precomputed) | O(rows×cols) | O(rows×cols) |

### 17. Count Paths with K Edges
Count paths with exactly K edges between two nodes.

| Approach | Time | Space |
|----------|------|-------|
| Brute Force DFS | O(V^k) | O(k) |
| Matrix Exponentiation | O(V³ log k) | O(V²) |

### 18. Minimum Cost Simple Path
Find minimum cost path between two nodes.

| Approach | Time | Space |
|----------|------|-------|
| Dijkstra-like | O(E log V) | O(V) |

### 19. Minimum Cost via Intermediates
Find minimum cost path via allowed intermediates.

| Approach | Time | Space |
|----------|------|-------|
| Floyd-Warshall | O(V³) | O(V²) |

---

## Topics Covered

- Stack using Queue
- Queue using Stacks
- BFS Graph Traversal
- Level Order Tree Traversal
- FIFO Page Replacement
- K Queues in Array
- Queue Reversal
- Reverse First K Elements
- First Non-Repeating Character
- Knight Moves (BFS)
- Sliding Window Maximum
- Binary Maze Shortest Path
- Generate Binary Numbers
- Snake & Ladder
- Shortest Safe Route with Landmines
- Count Paths with K Edges
- Minimum Cost Simple Path
- Minimum Cost via Intermediates (Floyd-Warshall)

---

## Usage

```bash
# Run individual test
python Queue/stack_using_queue.py
python Queue/queue_using_stacks.py

# Run all tests
for file in Queue/*.py; do python "$file"; done
```

---

## References

- [GeeksforGeeks Queue Data Structure](https://www.geeksforgeeks.org/queue-data-structure/)
- [GeeksforGeeks DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
