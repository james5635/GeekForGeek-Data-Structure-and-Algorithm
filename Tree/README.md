# Tree Data Structures - GeeksforGeeks Implementations

This folder contains Python implementations of various tree data structures and algorithms from GeeksforGeeks DSA tutorials.

## Table of Contents

| # | File | Topic |
|---|------|-------|
| 1 | [inorder_traversal.py](inorder_traversal.py) | Inorder Traversal (LNR) |
| 2 | [preorder_traversal.py](preorder_traversal.py) | Preorder Traversal (NLR) |
| 3 | [postorder_traversal.py](postorder_traversal.py) | Postorder Traversal (LRN) |
| 4 | [level_order_traversal.py](level_order_traversal.py) | Level Order Traversal (BFS) |
| 5 | [tree_height.py](tree_height.py) | Tree Height/Depth |
| 6 | [get_node_level.py](get_node_level.py) | Get Level of a Node |
| 7 | [search_node.py](search_node.py) | Search a Node in Binary Tree |
| 8 | [find_parent.py](find_parent.py) | Find Parent of a Node |
| 9 | [insert_level_order.py](insert_level_order.py) | Insert in Binary Tree (Level Order) |
| 10 | [delete_binary_tree.py](delete_binary_tree.py) | Delete from Binary Tree |
| 11 | [bst_search_insert.py](bst_search_insert.py) | BST Search and Insertion |
| 12 | [bst_traversal.py](bst_traversal.py) | BST Traversals |
| 13 | [bst_deletion.py](bst_deletion.py) | BST Deletion |
| 14 | [avl_insertion.py](avl_insertion.py) | AVL Tree Insertion |
| 15 | [red_black_insertion.py](red_black_insertion.py) | Red-Black Tree Insertion |
| 16 | [binary_tree_array.py](binary_tree_array.py) | Binary Tree Array Representation |

---

## Algorithm Details

### Binary Tree Traversals

| File | Approach | Time | Space |
|------|----------|------|-------|
| inorder_traversal.py | Recursive & Iterative | O(n) | O(h) / O(n) |
| preorder_traversal.py | Recursive & Iterative | O(n) | O(h) / O(n) |
| postorder_traversal.py | Recursive & Iterative | O(n) | O(h) / O(n) |
| level_order_traversal.py | Iterative (Queue) | O(n) | O(n) |

### Tree Properties & Queries

| File | Approach | Time | Space |
|------|----------|------|-------|
| tree_height.py | Recursive & Iterative | O(n) | O(h) / O(n) |
| get_node_level.py | Recursive & Iterative | O(n) | O(h) / O(n) |
| search_node.py | Recursive & Iterative | O(n) | O(h) / O(n) |
| find_parent.py | Recursive & Iterative | O(n) | O(h) / O(n) |

### Binary Tree Modification

| File | Approach | Time | Space |
|------|----------|------|-------|
| insert_level_order.py | Level Order Insertion | O(n) | O(n) |
| delete_binary_tree.py | Replace with Deepest Node | O(n) | O(n) |

### Binary Search Tree Operations

| File | Approach | Time | Space |
|------|----------|------|-------|
| bst_search_insert.py | BST Search/Insert | O(h) | O(h) / O(1) |
| bst_traversal.py | BST Traversals | O(n) | O(h) |
| bst_deletion.py | BST Deletion | O(h) | O(h) |

### Self-Balancing Trees

| File | Approach | Time | Space |
|------|----------|------|-------|
| avl_insertion.py | AVL Insertion (with rotations) | O(log n) | O(log n) |
| red_black_insertion.py | RB Insertion (with coloring) | O(log n) | O(log n) |

### Alternative Representations

| File | Approach | Time | Space |
|------|----------|------|-------|
| binary_tree_array.py | Array Representation | O(1) access | O(n) |

---

## Usage Examples

```bash
# Run traversal tests
python Tree/inorder_traversal.py
python Tree/preorder_traversal.py
python Tree/postorder_traversal.py
python Tree/level_order_traversal.py

# Run BST tests
python Tree/bst_search_insert.py
python Tree/bst_traversal.py
python Tree/bst_deletion.py

# Run self-balancing tree tests
python Tree/avl_insertion.py
python Tree/red_black_insertion.py
```

---

## Sample Outputs

### Traversals (Tree: 1(2(4,5),3(6)))
- **Inorder**: 4 2 5 1 3 6
- **Preorder**: 1 2 4 5 3 6  
- **Postorder**: 4 5 2 6 3 1
- **Level Order**: 1 2 3 4 5 6

### BST Operations (Insert: 6,2,8,7,9)
- **Search 7**: True
- **Search 14**: False
- **Inorder**: 2 6 7 8 9

### Tree Height (Tree: 1(2(4,5),3))
- **Height**: 2 (edges) or 3 (nodes)

---

## Topics Covered

- Binary Tree Traversals (Inorder, Preorder, Postorder, Level Order)
- Tree Properties (Height, Node Level, Search, Parent)
- Binary Tree Modification (Level Order Insertion, Deletion)
- Binary Search Tree Operations (Search, Insert, Traversal, Deletion)
- Self-Balancing Trees (AVL Insertion, Red-Black Tree Insertion)
- Alternative Representations (Binary Tree using Arrays)

---

## References

- [GeeksforGeeks Binary Tree](https://www.geeksforgeeks.org/binary-tree-data-structure/)
- [GeeksforGeeks Tree Traversals](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
- [GeeksforGeeks Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
- [GeeksforGeeks AVL Tree](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)
- [GeeksforGeeks Red-Black Tree](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction/)
- [GeeksforGeeks DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
