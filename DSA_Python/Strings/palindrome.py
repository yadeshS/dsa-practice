# strings/palindrome.py
# Palindrome = reads same forward and backward

s = "madam"

# Method 1: reverse using slicing
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")