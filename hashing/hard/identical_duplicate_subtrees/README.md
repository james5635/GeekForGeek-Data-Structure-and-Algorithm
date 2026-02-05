# Identical Duplicate Subtrees

## Problem Description

Given a binary tree, find all duplicate subtrees. Two subtrees are considered duplicates if they have the same structure and the same node values.

## Examples

```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```

**Output**: Two duplicate subtrees:
- Subtree with root 4 (appears 3 times)
- Subtree with root 2 (appears 2 times)

## Approach

### Serialization with Hash Map

1. **Serialize**: Convert each subtree to a string representation
2. **Hash**: Use hash map to count occurrences of each serialization
3. **Identify**: When count reaches 2, we found a duplicate

## Serialization Format

Pre-order traversal: `node_val,left_serial,right_serial`
- Empty node: `#`
- Example: Tree `2->4` serializes as: `"2,4,#,#,#"`

## Complexity Analysis

- **Time Complexity**: O(n) - visit each node once
- **Space Complexity**: O(n) - for hash map and recursion stack

## Key Insight

By serializing subtrees, we convert the tree comparison problem into string comparison. Hash map allows O(1) lookup to detect duplicates.

## Applications

1. **Code Duplication Detection**: Similar approach for AST comparison
2. **Plagiarism Detection**: Comparing program structures
3. **Tree Compression**: Identifying repeated patterns for optimization
