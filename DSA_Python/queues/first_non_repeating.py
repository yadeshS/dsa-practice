from collections import deque

def first_non_repeating(stream: str):
    q = deque()
    freq = {}

    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        while q and freq[q[0]] > 1:
            q.popleft()

        if q:
            print("First non-repeating:", q[0])
        else:
            print("First non-repeating: None")


# Test
first_non_repeating("aabc")