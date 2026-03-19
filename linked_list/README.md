# Linked List Algorithms Implementation

This folder contains Python implementations of various linked list algorithms from GeeksforGeeks.

## Table of Contents

- [Singly Linked List](#singly-linked-list)
- [Doubly Linked List](#doubly-linked-list)
- [Circular Linked List](#circular-linked-list)
- [Advanced Operations](#advanced-operations)
- [Special Cases](#special-cases)

## Singly Linked List

### Basic Operations
1. `node.py` - Node class definition
2. `linked_list.py` - Basic linked list implementation
3. `length_iterative.py` - Find length (iterative)
4. `length_recursive.py` - Find length (recursive)
5. `search_iterative.py` - Search element (iterative)
6. `search_recursive.py` - Search element (recursive)
7. `get_nth_node.py` - Get Nth node
8. `nth_node_from_end.py` - Nth node from end
9. `print_middle.py` - Print middle node
10. `count_occurrences.py` - Count occurrences of an element
11. `print_list.py` - Print linked list

### Insertion Operations
12. `insert_at_beginning.py` - Insert at beginning
13. `insert_at_end.py` - Insert at end
14. `insert_at_position.py` - Insert at position
15. `insert_sorted.py` - Insert in sorted way
16. `delete_node.py` - Delete a node
17. `delete_at_position.py` - Delete at position
18. `delete_list.py` - Delete entire list

### Modification Operations
19. `reverse.py` - Reverse linked list
20. `reverse_groups.py` - Reverse in groups of given size
21. `pairwise_swap.py` - Pairwise swap elements
22. `rotate.py` - Rotate linked list
23. `segregate_even_odd.py` - Segregate even and odd nodes

### Loop Detection
24. `detect_loop.py` - Detect loop using Floyd's algorithm
25. `find_loop_length.py` - Find length of loop

### Sorting Operations
26. `quicksort.py` - QuickSort on linked list
27. `merge_sort.py` - Merge sort for linked list

### Intersection & Union
28. `intersection_sorted.py` - Intersection of two sorted lists
29. `union_intersection.py` - Union and intersection

## Doubly Linked List

### Basic Operations
30. `dll_node.py` - Doubly linked list node class
31. `dll_implementation.py` - Basic DLL implementation
32. `dll_length.py` - Find size of DLL
33. `dll_reverse.py` - Reverse doubly linked list
34. `dll_reverse_groups.py` - Reverse DLL in groups
35. `delete_dll.py` - Delete a node in DLL
36. `remove_duplicates_sorted_dll.py` - Remove duplicates from sorted DLL
37. `remove_duplicates_unsorted_dll.py` - Remove duplicates from unsorted DLL
38. `insert_sorted_dll.py` - Insert value in sorted DLL
39. `pairs_with_sum_dll.py` - Find pairs with sum in DLL
40. `rotate_dll.py` - Rotate doubly linked list
41. `merge_dll.py` - Merge two sorted DLLs

## Circular Linked List

### Basic Operations
42. `cll_node.py` - Circular linked list node class
43. `cll_traversal.py` - Traversal of circular linked list
44. `cll_check_circular.py` - Check if linked list is circular
45. `cll_count.py` - Count nodes in circular linked list
46. `cll_delete.py` - Delete from circular linked list
47. `singly_to_circular.py` - Convert singly to circular
48. `exchange_first_last_cll.py` - Exchange first and last node

### Split Operations
49. `cll_split.py` - Split circular linked list into two halves

## Advanced Operations

### Merging
50. `merge_sorted.py` - Merge two sorted linked lists
51. `merge_k_sorted.py` - Merge K sorted linked lists

### Special Pointers
52. `intersection_point.py` - Find intersection point of two lists
53. `clone_arbit_pointer.py` - Clone linked list with arbitrary pointer
54. `delete_n_after_m.py` - Delete N nodes after M nodes

### Utility Operations
55. `remove_duplicates_unsorted.py` - Remove duplicates from unsorted list
56. `partition_list.py` - Partition list around a value
57. `sublist_search.py` - Sublist search
58. `remove_kth_node.py` - Remove every Kth node

## Special Cases

### Conversion Operations
59. `tree_to_dll.py` - Convert binary tree to doubly linked list
60. `construct_from_2d_matrix.py` - Construct linked list from 2D matrix

### Mathematical Operations
61. `multiply_linked_lists.py` - Multiply two numbers represented as lists
62. `block_wise_rotation.py` - Rotate linked list block-wise

### Edge Cases
63. `delete_without_head.py` - Delete node given only pointer to it

## Running the Code

```bash
python linked_list/<filename>.py
```

Each file contains test cases in `if __name__ == "__main__":` block.