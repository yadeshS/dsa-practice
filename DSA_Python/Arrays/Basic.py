arr = [10, 20, 30, 40, 50]

print("Array:", arr)
print("First element:", arr[0])   
print("Last element:", arr[-1])     
print("Length:", len(arr))          

# Traversal using index
print("\nTraversal using index:")
for i in range(len(arr)):
    print(f"Index {i} -> {arr[i]}")

# Traversal directly
print("\nTraversal directly:")
for num in arr:
    print(num)


arr.append(60)
print("\nAfter append(60):", arr)


arr.pop()
print("After pop():", arr)