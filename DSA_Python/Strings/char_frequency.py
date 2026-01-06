s = "hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1  # get(ch,0) returns 0 if not found

print("Frequency:", freq)