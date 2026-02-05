# Reconstruct Itinerary from List of Tickets

## Problem Statement
Given a list of tickets, find the itinerary in order. The input is not cyclic and there is one ticket from every city except the final destination.

## Approach
Use two HashMaps:
1. **Ticket Map**: Store from -> to mapping
2. **Reverse Map**: Store to -> from mapping
3. **Find Start**: City present in ticket map but not in reverse map
4. **Build Itinerary**: Follow tickets from start city

## Complexity
- **Time**: O(N) - Build maps and traverse once
- **Space**: O(N) - Two hash maps

## Example
```
Input: [Chennai, Bangalore], [Bombay, Delhi], [Goa, Chennai], [Delhi, Goa]
Output: Bombay -> Delhi -> Goa -> Chennai -> Bangalore
```
