"""
Program for Assigning Usernames using Trie

Given a queue of n users, assign a username to each. The system works as follows:
Every user has a preferred login string 's'. Usernames are assigned in order:
s, s0, s1, s2, ... s11, ... First check if s is available, if occupied check s0,
and so on. Once a username is assigned, it becomes occupied for subsequent users.

Uses a Trie with 36 children (26 alphabets + 10 digits) and an additional
struct to track if a node is a leaf and how many concatenations exist.

Time Complexity: O(n * m) where n is number of names, m is max name length
Space Complexity: O(n * m)
"""

MAX_CHAR = 26


class Additional:
    def __init__(self):
        self.is_set = False
        self.add = -1


class Trie:
    def __init__(self):
        self.character = [None] * MAX_CHAR
        self.number = [None] * 10
        self.a = Additional()


def get_new():
    """Create and return a new Trie node."""
    return Trie()


def insert(head, s):
    """Insert a string into the Trie."""
    curr = head
    for ch in s:
        if ord(ch) - ord("a") < 0:
            if curr.number[int(ch)] is None:
                curr.number[int(ch)] = get_new()
            curr = curr.number[int(ch)]
        else:
            if curr.character[ord(ch) - ord("a")] is None:
                curr.character[ord(ch) - ord("a")] = get_new()
            curr = curr.character[ord(ch) - ord("a")]
    curr.a.is_set = True


def search(head, s):
    """Search for a string in the Trie. Returns Additional struct."""
    x = Additional()
    x.is_set = False
    x.add = -1

    if head is None:
        return x

    curr = head
    for ch in s:
        if ord(ch) - ord("a") < 0:
            curr = curr.number[int(ch)]
        else:
            curr = curr.character[ord(ch) - ord("a")]
        if curr is None:
            return x

    x.is_set = curr.a.is_set
    x.add = curr.a.add
    return x


def update(head, s, z):
    """Update the add variable at the end of string s to z."""
    curr = head
    for ch in s:
        if ord(ch) - ord("a") < 0:
            curr = curr.number[int(ch)]
        else:
            curr = curr.character[ord(ch) - ord("a")]
    curr.a.add = z


def assign_usernames(username):
    """
    Assign unique usernames to users in the order they appear.

    Args:
        username: List of preferred usernames

    Returns:
        List of assigned usernames
    """
    head = get_new()
    assigned = []

    for s in username:
        x = search(head, s)

        if not x.is_set:
            assigned.append(s)
            insert(head, s)
        else:
            y = x.add + 1
            t = s

            while True:
                if not search(head, t + str(y)).is_set:
                    assigned.append(t + str(y))
                    insert(head, t + str(y))
                    update(head, s, y)
                    break
                else:
                    y += 1

    return assigned


if __name__ == "__main__":
    names1 = ["abc", "bcd"]
    result1 = assign_usernames(names1)
    print(f"Input: {names1}")
    print(f"Output: {result1}")
    print()

    names2 = ["abc", "bcd", "abc"]
    result2 = assign_usernames(names2)
    print(f"Input: {names2}")
    print(f"Output: {result2}")
    print()

    names3 = ["geek", "geek0", "geek1", "geek"]
    result3 = assign_usernames(names3)
    print(f"Input: {names3}")
    print(f"Output: {result3}")
