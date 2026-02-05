"""
Data Structure with O(1) Operations

Problem: Design a data structure that supports insert, delete, search, and getRandom
operations in O(1) time complexity.

Approach: Use a hash map to store value-to-index mapping and a list to store values.
For delete, swap with last element to maintain O(1) removal from list.

Time Complexity: O(1) for all operations
Space Complexity: O(n) for storing n elements
"""

import random


class RandomizedSet:
    """
    A data structure supporting O(1) insert, delete, search, and getRandom.
    """

    def __init__(self):
        """Initialize the data structure."""
        self.value_to_index = {}
        self.values = []

    def insert(self, val):
        """
        Insert a value into the set.

        Args:
            val: Value to insert

        Returns:
            True if inserted, False if already exists
        """
        if val in self.value_to_index:
            return False

        self.value_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Remove a value from the set.

        Args:
            val: Value to remove

        Returns:
            True if removed, False if not found
        """
        if val not in self.value_to_index:
            return False

        # Get index of element to remove
        idx = self.value_to_index[val]
        last_idx = len(self.values) - 1
        last_val = self.values[last_idx]

        # Swap with last element
        self.values[idx] = last_val
        self.value_to_index[last_val] = idx

        # Remove last element
        self.values.pop()
        del self.value_to_index[val]

        return True

    def search(self, val):
        """
        Search for a value in the set.

        Args:
            val: Value to search

        Returns:
            True if exists, False otherwise
        """
        return val in self.value_to_index

    def get_random(self):
        """
        Get a random element from the set.

        Returns:
            Random element from the set
        """
        if not self.values:
            return None
        return random.choice(self.values)

    def get_all(self):
        """
        Get all elements in the set.

        Returns:
            List of all elements
        """
        return self.values.copy()

    def size(self):
        """
        Get the size of the set.

        Returns:
            Number of elements
        """
        return len(self.values)


class RandomizedDict:
    """
    A data structure supporting O(1) operations with key-value pairs.
    """

    def __init__(self):
        """Initialize the data structure."""
        self.key_to_index = {}
        self.keys = []
        self.values = []

    def insert(self, key, value):
        """
        Insert a key-value pair.

        Args:
            key: Key to insert
            value: Value to associate

        Returns:
            True if inserted, False if key already exists
        """
        if key in self.key_to_index:
            return False

        self.key_to_index[key] = len(self.keys)
        self.keys.append(key)
        self.values.append(value)
        return True

    def remove(self, key):
        """
        Remove a key-value pair.

        Args:
            key: Key to remove

        Returns:
            True if removed, False if not found
        """
        if key not in self.key_to_index:
            return False

        idx = self.key_to_index[key]
        last_idx = len(self.keys) - 1
        last_key = self.keys[last_idx]

        # Swap with last element
        self.keys[idx] = last_key
        self.values[idx] = self.values[last_idx]
        self.key_to_index[last_key] = idx

        # Remove last element
        self.keys.pop()
        self.values.pop()
        del self.key_to_index[key]

        return True

    def search(self, key):
        """
        Search for a key.

        Args:
            key: Key to search

        Returns:
            Value if found, None otherwise
        """
        if key in self.key_to_index:
            idx = self.key_to_index[key]
            return self.values[idx]
        return None

    def get_random(self):
        """
        Get a random key-value pair.

        Returns:
            Tuple of (key, value) or None
        """
        if not self.keys:
            return None
        idx = random.randint(0, len(self.keys) - 1)
        return (self.keys[idx], self.values[idx])

    def update(self, key, value):
        """
        Update value for existing key.

        Args:
            key: Key to update
            value: New value

        Returns:
            True if updated, False if key not found
        """
        if key in self.key_to_index:
            idx = self.key_to_index[key]
            self.values[idx] = value
            return True
        return False


if __name__ == "__main__":
    print("=== RandomizedSet Demo ===")
    rs = RandomizedSet()

    # Test Insert
    print("Inserting: 1, 2, 3")
    rs.insert(1)
    rs.insert(2)
    rs.insert(3)
    print(f"All elements: {rs.get_all()}")

    # Test Search
    print(f"Search 2: {rs.search(2)}")
    print(f"Search 5: {rs.search(5)}")

    # Test Random
    print(f"Random element: {rs.get_random()}")

    # Test Remove
    print(f"Remove 2: {rs.remove(2)}")
    print(f"All elements after removal: {rs.get_all()}")
    print(f"Search 2 after removal: {rs.search(2)}")

    print("\n=== RandomizedDict Demo ===")
    rd = RandomizedDict()

    # Test Insert
    print("Inserting: (a, 1), (b, 2), (c, 3)")
    rd.insert("a", 1)
    rd.insert("b", 2)
    rd.insert("c", 3)

    # Test Search
    print(f"Search 'b': {rd.search('b')}")

    # Test Update
    rd.update("b", 20)
    print(f"Search 'b' after update: {rd.search('b')}")

    # Test Random
    print(f"Random pair: {rd.get_random()}")

    # Test Remove
    print(f"Remove 'b': {rd.remove('b')}")
    print(f"Search 'b' after removal: {rd.search('b')}")

    print("\n=== Edge Cases ===")
    # Empty set operations
    empty_set = RandomizedSet()
    print(f"Random from empty: {empty_set.get_random()}")
    print(f"Remove from empty: {empty_set.remove(1)}")

    # Duplicate insert
    rs2 = RandomizedSet()
    rs2.insert(1)
    print(f"Insert 1 again: {rs2.insert(1)}")

    # Remove non-existent
    print(f"Remove 999: {rs2.remove(999)}")
