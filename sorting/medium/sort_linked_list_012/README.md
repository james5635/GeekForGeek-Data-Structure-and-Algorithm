# Sort a Linked List of 0s, 1s, and 2s

## Problem Description

Given a linked list containing only 0s, 1s, and 2s, sort the linked list in non-decreasing order.

## Examples

### Example 1
- **Input:** `1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL`
- **Output:** `0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL`

### Example 2
- **Input:** `1 -> 1 -> 2 -> 1 -> 0 -> NULL`
- **Output:** `0 -> 1 -> 1 -> 1 -> 2 -> NULL`

## Approaches

### Approach 1: Counting (Data Change)

1. Traverse the list and count occurrences of 0, 1, and 2
2. Traverse again and overwrite node values based on counts
3. First `count[0]` nodes become 0, next `count[1]` nodes become 1, rest become 2

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Approach 2: Dutch National Flag (Link Change) ⭐ Recommended

1. Create three separate linked lists for 0s, 1s, and 2s using dummy nodes
2. Traverse original list and append each node to appropriate list
3. Connect the three lists: zeros -> ones -> twos
4. Set tail's next to NULL

**Time Complexity:** O(n)
**Space Complexity:** O(1)

## Comparison

| Approach | Time | Space | Modifies |
|----------|------|-------|----------|
| Counting | O(n) | O(1) | Data only |
| Dutch National Flag | O(n) | O(1) | Links only |

## Key Points

- **Dutch National Flag advantage:** Doesn't modify data, only rearranges links
- Useful when node data is large or shouldn't be modified
- Both approaches are single-pass (or two-pass for counting)
- Dummy nodes simplify implementation by avoiding null checks

## Related Problems

- Sort array of 0s, 1s, and 2s
- Dutch National Flag problem
- Segregate even and odd nodes in linked list

## References

- [GeeksforGeeks - Sort Linked List 0s 1s 2s](https://www.geeksforgeeks.org/dsa/sort-a-linked-list-of-0s-1s-or-2s/)
