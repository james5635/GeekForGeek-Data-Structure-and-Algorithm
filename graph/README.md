# Graph Data Structure & Algorithms

Complete collection of Graph algorithms and data structure implementations in Python, based on [GeeksForGeeks DSA Tutorial](https://www.geeksforgeeks.org/dsa/graph-data-structure/).

## Table of Contents

- [Graph Traversal](#graph-traversal)
- [Topological Sort](#topological-sort)
- [Graph Utility](#graph-utility)
- [BFS Applications](#bfs-applications)
- [Cycle Detection](#cycle-detection)
- [Disjoint Set Union-Find](#disjoint-set-union-find)
- [Shortest Path](#shortest-path)
- [Minimum Spanning Tree](#minimum-spanning-tree)
- [Advanced Graph Algorithms](#advanced-graph-algorithms)
- [Maximum Flow](#maximum-flow)
- [NP-Hard Problems](#np-hard-problems)

---

## Graph Traversal

| Algorithm | File | Description |
|-----------|------|-------------|
| Graph Representation | `traversal/graph_representation.py` | Adjacency list & matrix implementations, directed/undirected, weighted/unweighted |
| DFS Traversal | `traversal/dfs_traversal.py` | Depth-first search - recursive & iterative, handles disconnected graphs |
| BFS Traversal | `traversal/bfs_traversal.py` | Breadth-first search - handles disconnected graphs |
| Shortest Path (Unweighted) | `traversal/shortest_path_unweighted.py` | BFS-based shortest path with path reconstruction |
| 0-1 BFS | `traversal/zero_one_bfs.py` | Shortest path in binary-weighted graphs using deque, O(V+E) |

## Topological Sort

| Algorithm | File | Description |
|-----------|------|-------------|
| Topological Sort (DFS) | `topological_sort/topological_sort_dfs.py` | DFS-based topological ordering with cycle detection |
| All Topological Sorts | `topological_sort/all_topological_sorts.py` | Enumerate all valid topological orderings of a DAG |
| Kahn's Algorithm | `topological_sort/kahns_algorithm.py` | BFS-based topological sort using in-degree counting |
| Sum of Dependencies | `topological_sort/sum_of_dependencies.py` | Compute total and per-node dependency counts |
| Maximum Weight Node | `topological_sort/maximum_weight_node.py` | Find node with maximum incoming weight sum |

## Graph Utility

| Algorithm | File | Description |
|-----------|------|-------------|
| Transitive Closure | `utility/transitive_closure.py` | Floyd-Warshall based transitive closure, O(V^3) |
| Count Trees in Forest | `utility/count_trees_in_forest.py` | Count connected components using DFS/BFS |

## BFS Applications

| Algorithm | File | Description |
|-----------|------|-------------|
| Rotten Oranges | `bfs_applications/rotten_oranges.py` | Multi-source BFS - minimum time to rot all oranges |
| Number of Islands | `bfs_applications/number_of_islands.py` | Count connected components in 2D grid (8-directional) |
| Flood Fill | `bfs_applications/flood_fill.py` | Replace connected same-color pixels |
| Bipartite Graph | `bfs_applications/is_bipartite.py` | 2-coloring check using BFS |
| Word Ladder | `bfs_applications/word_ladder.py` | Shortest transformation sequence between words |
| Snake and Ladder | `bfs_applications/snake_and_ladder.py` | Minimum dice throws to reach end |
| Water Jug Problem | `bfs_applications/water_jug.py` | State-space BFS to measure target amount |
| Shortest Path in Binary Matrix | `bfs_applications/shortest_path_binary_matrix.py` | 8-directional BFS through clear cells |
| Clone Graph | `bfs_applications/clone_graph.py` | Deep copy of undirected graph |
| Largest Region in Boolean Matrix | `bfs_applications/largest_region_boolean_matrix.py` | Find maximum area connected component |
| Shortest Word Chain | `bfs_applications/shortest_word_chain.py` | BFS word graph for shortest chain |
| Pacific Atlantic Water Flow | `bfs_applications/pacific_atlantic_water_flow.py` | Reverse BFS from ocean edges |
| Boggle Word Search | `bfs_applications/boggle_word_search.py` | DFS backtracking with Trie for word search |

## Cycle Detection

| Algorithm | File | Description |
|-----------|------|-------------|
| Cycle in Directed Graph | `cycle_detection/detect_cycle_directed.py` | DFS with 3-color marking, O(V+E) |
| Cycle in Undirected Graph | `cycle_detection/detect_cycle_undirected.py` | DFS/BFS with parent tracking, O(V+E) |
| Negative Cycle (Bellman-Ford) | `cycle_detection/detect_negative_cycle_bellman_ford.py` | Detect negative weight cycles using relaxation |
| Cycles of Length N | `cycle_detection/cycles_of_length_n.py` | Enumerate all simple cycles of length n |
| Negative Cycle (Floyd-Warshall) | `cycle_detection/detect_negative_cycle_floyd_warshall.py` | Detect via diagonal check in all-pairs shortest paths |
| Clone Directed Acyclic Graph | `cycle_detection/clone_directed_acyclic_graph.py` | DFS-based deep copy of DAG |
| Clone Undirected Graph | `cycle_detection/clone_undirected_graph.py` | BFS/DFS deep copy with cycle handling |

## Disjoint Set Union-Find

| Algorithm | File | Description |
|-----------|------|-------------|
| Disjoint Set Union-Find | `disjoint_set/disjoint_set_union_find.py` | Basic Union-Find with find(), union(), is_connected() |
| Union by Rank & Path Compression | `disjoint_set/union_by_rank_path_compression.py` | Optimized Union-Find with rank/size heuristics, O(alpha(n)) |

## Shortest Path

| Algorithm | File | Description |
|-----------|------|-------------|
| Dijkstra's Algorithm | `shortest_path/dijkstra.py` | Single-source shortest path, non-negative weights |
| Bellman-Ford | `shortest_path/bellman_ford.py` | Single-source with negative edge detection |
| Floyd-Warshall | `shortest_path/floyd_warshall.py` | All-pairs shortest paths, handles negative edges |
| Johnson's Algorithm | `shortest_path/johnsons_algorithm.py` | All-pairs shortest paths for sparse graphs |
| Multistage Graph | `shortest_path/multistage_graph_shortest_path.py` | Forward & backward DP for multistage graphs |
| Karp's Minimum Mean Weight Cycle | `shortest_path/karps_minimum_mean_weight_cycle.py` | Find minimum mean weight cycle in directed graph |
| Minimum Weight Cycle (Undirected) | `shortest_path/minimum_weight_cycle_undirected.py` | Dijkstra-based minimum cycle detection |

## Minimum Spanning Tree

| Algorithm | File | Description |
|-----------|------|-------------|
| Prim's MST | `minimum_spanning_tree/prims_mst.py` | Greedy vertex-based MST using min-heap, O((V+E)logV) |
| Kruskal's MST | `minimum_spanning_tree/kruskals_mst.py` | Greedy edge-based MST using Union-Find, O(E log E) |
| Min Cost Connect Cities | `minimum_spanning_tree/minimum_cost_connect_cities.py` | Connect all cities with minimum cost |
| Minimum Product Spanning Tree | `minimum_spanning_tree/minimum_product_spanning_tree.py` | Log transformation + Prim's to minimize product |
| Reverse Delete MST | `minimum_spanning_tree/reverse_delete_mst.py` | Remove heaviest edges while maintaining connectivity |
| Boruvka's MST | `minimum_spanning_tree/boruvkas_mst.py` | Parallel MST algorithm, O(E log V) |

## Advanced Graph Algorithms

| Algorithm | File | Description |
|-----------|------|-------------|
| Max Edges in DAG | `advanced/max_edges_to_add_dag.py` | Maximum edges that can be added while maintaining DAG |
| Longest Path in DAG | `advanced/longest_path_in_dag.py` | Find longest path using topological sort |
| Topological Sort (Departure Time) | `advanced/topological_sort_departure_time.py` | Sort by DFS departure times |
| Find Itinerary from Tickets | `advanced/find_itinerary_from_tickets.py` | Reconstruct itinerary from ticket pairs |
| Eulerian Path & Circuit | `advanced/eulerian_path_and_circuit.py` | Check for Eulerian path/circuit existence |
| Fleury's Algorithm | `advanced/fleurys_algorithm.py` | Print Eulerian path/circuit by avoiding bridges |
| Strongly Connected Components | `advanced/strongly_connected_components.py` | Kosaraju's algorithm for SCC |
| Count Walks with K Edges | `advanced/count_walks_with_k_edges.py` | Matrix exponentiation for counting walks |
| Euler Circuit (Directed) | `advanced/euler_circuit_directed_graph.py` | Check Euler circuit in directed graph |
| Seven Bridges of Konigsberg | `advanced/seven_bridges_konigsberg.py` | Historical Eulerian path problem |
| Dynamic Connectivity | `advanced/dynamic_connectivity_incremental.py` | Incremental connectivity using Union-Find |
| Construct Graph from Degrees | `advanced/construct_graph_from_degrees.py` | Havel-Hakimi algorithm for degree sequence |
| Universal Sink Detection | `advanced/universal_sink_detection.py` | Find node with in-degree V-1 and out-degree 0 |
| Number of Sink Nodes | `advanced/number_of_sink_nodes.py` | Count nodes with out-degree 0 |
| Two Clique Problem | `advanced/two_clique_problem.py` | Check if graph can be divided into two cliques |
| Total Spanning Trees | `advanced/total_spanning_trees.py` | Matrix Tree Theorem implementation |
| Bridges in Graph | `advanced/bridges_in_graph.py` | Find all bridge edges using DFS |
| Articulation Points | `advanced/articulation_points.py` | Find all cut vertices using DFS |
| Biconnected Components | `advanced/biconnected_components.py` | Find biconnected components using stack |
| String Chain Circle | `advanced/string_chain_circle.py` | Check if strings can form a circular chain |
| Tarjan's SCC | `advanced/tarjans_scc.py` | Tarjan's algorithm for strongly connected components |
| Peterson Graph | `advanced/petersen_graph.py` | Peterson graph path problem |
| Erdos-Renyi Model | `advanced/erdos_renyi_model.py` | Generate random graphs using Erdos-Renyi model |
| Chinese Postman | `advanced/chinese_postman.py` | Route inspection problem |
| Hierholzer's Algorithm | `advanced/hierholzers_algorithm.py` | Find Eulerian circuit in directed graph |
| Graph Coloring | `advanced/graph_coloring.py` | Greedy graph coloring algorithm |

## Maximum Flow

| Algorithm | File | Description |
|-----------|------|-------------|
| Max Flow Introduction | `max_flow/max_flow_intro.py` | Introduction to max flow with Ford-Fulkerson |
| Ford-Fulkerson | `max_flow/ford_fulkerson.py` | Maximum flow using augmenting paths |
| Maximum Edge Disjoint Paths | `max_flow/max_edge_disjoint_paths.py` | Find max number of edge-disjoint paths |
| Maximum Bipartite Matching | `max_flow/maximum_bipartite_matching.py` | DFS-based bipartite matching |
| Channel Assignment | `max_flow/channel_assignment.py` | Assign channels using bipartite matching |
| Karger's Algorithm | `max_flow/kargers_algorithm.py` | Randomized minimum cut algorithm |
| Dinic's Algorithm | `max_flow/dinics_algorithm.py` | Efficient max flow using level graphs |
| Minimum s-t Cut | `max_flow/minimum_st_cut.py` | Find minimum cut in flow network |

## NP-Hard Problems

| Algorithm | File | Description |
|-----------|------|-------------|
| Travelling Salesman Problem | `np_hard/travelling_salesman.py` | TSP with DP O(n^2 * 2^n) and brute force |
| Vertex Cover | `np_hard/vertex_cover.py` | 2-approximate greedy vertex cover |
| K Centers Problem | `np_hard/k_centers.py` | 2-approximate greedy k-centers algorithm |

---

## Usage

Each file is self-contained and can be run independently:

```bash
python graph/traversal/dfs_traversal.py
python graph/shortest_path/dijkstra.py
python graph/minimum_spanning_tree/prims_mst.py
```

## Complexity Summary

| Category | Best Algorithm | Worst Time Complexity |
|----------|---------------|----------------------|
| Traversal | DFS/BFS | O(V + E) |
| Shortest Path (non-negative) | Dijkstra | O((V + E) log V) |
| Shortest Path (with negative) | Bellman-Ford | O(V * E) |
| All-Pairs Shortest Path | Floyd-Warshall | O(V^3) |
| MST | Prim's/Kruskal's | O((V + E) log V) / O(E log E) |
| Max Flow | Dinic's | O(V^2 * E) |
| Topological Sort | Kahn's/DFS | O(V + E) |
| SCC | Tarjan's/Kosaraju's | O(V + E) |
| Bipartite Matching | Hopcroft-Karp | O(E * sqrt(V)) |
| TSP | DP (Held-Karp) | O(n^2 * 2^n) |

## Sources

- [GeeksForGeeks - Graph Data Structure](https://www.geeksforgeeks.org/dsa/graph-data-structure/)
- [GeeksForGeeks DSA Problems](https://www.geeksforgeeks.org/dsa/)
