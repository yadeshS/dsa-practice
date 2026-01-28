def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != pairs.get(ch):
                return False
            stack.pop()

    return len(stack) == 0


# Test
print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("((("))       # False