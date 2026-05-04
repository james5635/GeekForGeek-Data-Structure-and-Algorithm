def is_sum_string(s: str) -> bool:
    """Check if given string is a sum string where each digit/number is sum of previous two."""

    def add_strings(n1: str, n2: str) -> str:
        if len(n1) > 1 and n1[0] == "0":
            return ""
        if len(n2) > 1 and n2[0] == "0":
            return ""
        return str(int(n1) + int(n2))

    def check(n1: str, n2: str, remaining: str) -> bool:
        if not remaining:
            return True
        sum_str = add_strings(n1, n2)
        if remaining.startswith(sum_str):
            return check(n2, sum_str, remaining[len(sum_str) :])
        return False

    n = len(s)
    for i in range(1, n):
        for j in range(i + 1, n):
            n1, n2 = s[:i], s[i:j]
            if len(n1) > 1 and n1[0] == "0":
                continue
            if len(n2) > 1 and n2[0] == "0":
                continue
            if check(n1, n2, s[j:]):
                return True
    return False


if __name__ == "__main__":
    s1 = "1235813"
    print(f"'{s1}' is sum string: {is_sum_string(s1)}")
    s2 = "12131528"
    print(f"'{s2}' is sum string: {is_sum_string(s2)}")
    s3 = "234"
    print(f"'{s3}' is sum string: {is_sum_string(s3)}")
