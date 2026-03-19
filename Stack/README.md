# Stack Data Structure & Algorithms

Python implementations of Stack data structure and related algorithms from [GeeksforGeeks](https://www.geeksforgeeks.org/dsa/introduction-to-stack-data-structure-and-algorithm-tutorials/).

## Stack Implementations

| File | Description |
|------|-------------|
| [stack_using_array.py](stack_using_array.py) | Stack using Python list |
| [stack_using_linked_list.py](stack_using_linked_list.py) | Stack using singly linked list |
| [stack_using_deque.py](stack_using_deque.py) | Stack using `collections.deque` |
| [two_stacks_in_array.py](two_stacks_in_array.py) | Two stacks in a single array |
| [queue_using_stacks.py](queue_using_stacks.py) | Queue implementation using two stacks |
| [stack_using_queue.py](stack_using_queue.py) | Stack implementation using a queue |
| [k_stacks_in_array.py](k_stacks_in_array.py) | K stacks efficiently in a single array |
| [mergable_stack.py](mergable_stack.py) | Mergable stack that supports merge operation |

## Expression Conversion & Evaluation

| File | Description |
|------|-------------|
| [infix_to_postfix.py](infix_to_postfix.py) | Convert infix expression to postfix |
| [infix_to_prefix.py](infix_to_prefix.py) | Convert infix expression to prefix |
| [prefix_to_infix.py](prefix_to_infix.py) | Convert prefix expression to infix |
| [prefix_to_postfix.py](prefix_to_postfix.py) | Convert prefix expression to postfix |
| [postfix_to_infix.py](postfix_to_infix.py) | Convert postfix expression to infix |
| [postfix_to_prefix.py](postfix_to_prefix.py) | Convert postfix expression to prefix |
| [evaluate_postfix.py](evaluate_postfix.py) | Evaluate postfix expression |
| [balanced_parentheses.py](balanced_parentheses.py) | Check for balanced parentheses |
| [redundant_brackets.py](redundant_brackets.py) | Detect redundant brackets in expression |
| [remove_brackets.py](remove_brackets.py) | Remove brackets from algebraic string |
| [find_closing_bracket.py](find_closing_bracket.py) | Find closing bracket for given opening bracket |

## Stack Problem Solving

| File | Description |
|------|-------------|
| [celebrity_problem.py](celebrity_problem.py) | The Celebrity Problem |
| [reverse_stack.py](reverse_stack.py) | Reverse a stack using recursion |
| [reverse_stack_iterative.py](reverse_stack_iterative.py) | Reverse a stack using temporary stack |
| [reverse_stack_without_extra_space.py](reverse_stack_without_extra_space.py) | Reverse stack without extra space |
| [reverse_first_k_of_queue.py](reverse_first_k_of_queue.py) | Reverse first k elements of a queue |
| [sort_stack_using_temp_stack.py](sort_stack_using_temp_stack.py) | Sort a stack using temporary stack |
| [delete_middle_element.py](delete_middle_element.py) | Delete middle element of a stack |
| [check_queue_sortable.py](check_queue_sortable.py) | Check if queue can be sorted with stack |
| [check_array_stack_sortable.py](check_array_stack_sortable.py) | Check if array is stack sortable |
| [stack_permutations.py](stack_permutations.py) | Stack permutations check |
| [delete_consecutive_words.py](delete_consecutive_words.py) | Delete consecutive duplicate words |

## Monotonic Stack Problems

| File | Description |
|------|-------------|
| [nearest_smaller_on_left.py](nearest_smaller_on_left.py) | Nearest smaller numbers on left side |
| [next_greater_element.py](next_greater_element.py) | Next Greater Element for each element |
| [next_smaller_next_greater.py](next_smaller_next_greater.py) | Next smaller and next greater for every element |
| [next_greater_frequency_element.py](next_greater_frequency_element.py) | Next Greater Frequency Element |
| [stock_span_problem.py](stock_span_problem.py) | Stock Span Problem |
| [buildings_facing_sun.py](buildings_facing_sun.py) | Count buildings facing the sun |
| [largest_rectangle_histogram.py](largest_rectangle_histogram.py) | Largest rectangular area in histogram |
| [sum_of_max_of_subarrays.py](sum_of_max_of_subarrays.py) | Sum of max elements of all sub-arrays |
| [max_of_mins_every_window.py](max_of_mins_every_window.py) | Maximum of minimums for every window size |
| [max_diff_nearest_left_right_smaller.py](max_diff_nearest_left_right_smaller.py) | Max diff between nearest left/right smaller |
| [max_product_next_greater_left_right.py](max_product_next_greater_left_right.py) | Max product of next greater indices |
| [iterative_tower_of_hanoi.py](iterative_tower_of_hanoi.py) | Iterative Tower of Hanoi |

## Special Stack Designs

| File | Description |
|------|-------------|
| [getmin_in_o1.py](getmin_in_o1.py) | Stack with O(1) getMin operation |
| [customized_data_structure.py](customized_data_structure.py) | Stack with O(1) getMin and getMax |
| [max_frequency_stack.py](max_frequency_stack.py) | Stack returning max frequency element |
| [longest_valid_parentheses.py](longest_valid_parentheses.py) | Longest valid parentheses substring |

## Running

```bash
python Stack/<filename>.py
```

## Key Concepts

- **Stack**: LIFO (Last In First Out) data structure
- **Monotonic Stack**: Stack maintaining elements in sorted order; used for next greater/smaller element problems
- **Expression Conversion**: Infix, Prefix, Postfix notations and conversions using operator precedence and associativity
- **Balanced Parentheses**: Matching opening and closing brackets using stack
