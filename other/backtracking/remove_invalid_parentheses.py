def remove_invalid_parentheses(s: str) -> list[str]:
    """Remove minimum number of invalid parentheses to make string valid."""

    def is_valid(s: str) -> bool:
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0

    result = []
    visited = {s}
    queue = [s]
    found = False

    while queue:
        next_queue = []
        for curr in queue:
            if is_valid(curr):
                result.append(curr)
                found = True
            if not found:
                for i in range(len(curr)):
                    if curr[i] in "()":
                        next_s = curr[:i] + curr[i + 1 :]
                        if next_s not in visited:
                            visited.add(next_s)
                            next_queue.append(next_s)
        if found:
            break
        queue = next_queue

    return result if result else [""]


if __name__ == "__main__":
    s1 = "()())()"
    print(f"Input: {s1}")
    print(f"Output: {remove_invalid_parentheses(s1)}")
    s2 = "(a)())()"
    print(f"Input: {s2}")
    print(f"Output: {remove_invalid_parentheses(s2)}")
