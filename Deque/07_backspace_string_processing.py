from collections import deque


def process_backspace(s):
    dq = deque()
    for ch in s:
        if ch == "#":
            if dq:
                dq.pop()
        else:
            dq.append(ch)
    return "".join(dq)


if __name__ == "__main__":
    assert process_backspace("##geeks##for##geeks#") == "geefgeek"
    assert process_backspace("ab#c") == "ac"
    assert process_backspace("ab##c") == "c"
    assert process_backspace("a#c") == "c"
    assert process_backspace("###abc") == "abc"
    assert process_backspace("abc###") == ""
    assert process_backspace("") == ""
    assert process_backspace("a#b#c#") == ""
    assert process_backspace("abc#de##f") == "abf"

    print("All tests passed")
