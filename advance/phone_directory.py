"""
Implement a Phone Directory Using Trie

Given a list of contacts, implement a search query for the phone directory.
The search query on a string 'str' displays all contacts which have 'str' as
a prefix. Suggestions are shown after each character is entered.

Approach: Use a Trie data structure to store all contacts. For each prefix
of the query string, perform a DFS traversal from the corresponding Trie node
to find all contacts with that prefix.

Time Complexity: O(n * m) where n is number of contacts and m is max contact length
Auxiliary Space: O(n * m)

Source: https://www.geeksforgeeks.org/dsa/implement-a-phone-directory/
"""


class TrieNode:
    """A node in the Trie data structure."""

    def __init__(self):
        self.children = {}
        self.is_last = False


class PhoneDirectory:
    """Phone directory implementation using Trie for efficient prefix search."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, contact):
        """Insert a contact into the phone directory.

        Args:
            contact: A string representing a contact name.
        """
        itr = self.root
        for char in contact:
            if char not in itr.children:
                itr.children[char] = TrieNode()
            itr = itr.children[char]
        itr.is_last = True

    def insert_contacts(self, contacts):
        """Insert multiple contacts into the phone directory.

        Args:
            contacts: A list of contact name strings.
        """
        for contact in contacts:
            self.insert(contact)

    def _display_contacts_util(self, cur_node, prefix):
        """DFS traversal to display all contacts under a given Trie node.

        Args:
            cur_node: Current TrieNode being visited.
            prefix: String built from root to cur_node.
        """
        suggestions = []
        if cur_node.is_last:
            suggestions.append(prefix)

        for char_code in range(ord("a"), ord("z") + 1):
            char = chr(char_code)
            next_node = cur_node.children.get(char)
            if next_node:
                suggestions.extend(
                    self._display_contacts_util(next_node, prefix + char)
                )

        return suggestions

    def display_contacts(self, query):
        """Display suggestions after each character of the query string.

        Args:
            query: The search string entered character by character.

        Returns:
            A dictionary mapping each prefix to its list of suggestions.
        """
        prev_node = self.root
        prefix = ""
        results = {}

        for i, char in enumerate(query):
            prefix += char
            cur_node = prev_node.children.get(char)

            if cur_node is None:
                results[prefix] = []
                for remaining_char in query[i + 1 :]:
                    prefix += remaining_char
                    results[prefix] = []
                break

            suggestions = self._display_contacts_util(cur_node, prefix)
            results[prefix] = sorted(suggestions)
            prev_node = cur_node

        return results

    def search(self, prefix):
        """Search for contacts with a given prefix.

        Args:
            prefix: The prefix string to search for.

        Returns:
            A sorted list of contacts that start with the given prefix.
        """
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return []
            cur_node = cur_node.children[char]

        suggestions = self._display_contacts_util(cur_node, prefix)
        return sorted(suggestions)


if __name__ == "__main__":
    print("Test Case 1:")
    contacts = ["gforgeeks", "geeksquiz"]
    print(f"Contacts: {contacts}")

    directory = PhoneDirectory()
    directory.insert_contacts(contacts)

    query = "gekk"
    print(f"\nQuery: '{query}'")
    results = directory.display_contacts(query)

    for prefix, suggestions in results.items():
        if suggestions:
            print(f"  Suggestions based on '{prefix}':")
            for s in suggestions:
                print(f"    {s}")
        else:
            print(f"  No Results Found for '{prefix}'")

    print("\n" + "=" * 50)
    print("Test Case 2:")
    contacts2 = ["geezer", "geek", "geeksforgeeks", "geeksquiz", "gfor"]
    print(f"Contacts: {contacts2}")

    directory2 = PhoneDirectory()
    directory2.insert_contacts(contacts2)

    for prefix in ["g", "ge", "gee", "geek", "geeks"]:
        suggestions = directory2.search(prefix)
        print(f"  Search '{prefix}': {suggestions}")

    print("\n" + "=" * 50)
    print("Test Case 3 (no matching contacts):")
    contacts3 = ["alice", "bob", "charlie"]
    print(f"Contacts: {contacts3}")

    directory3 = PhoneDirectory()
    directory3.insert_contacts(contacts3)

    query3 = "xyz"
    results3 = directory3.display_contacts(query3)
    for prefix, suggestions in results3.items():
        if suggestions:
            print(f"  Suggestions based on '{prefix}': {suggestions}")
        else:
            print(f"  No Results Found for '{prefix}'")
