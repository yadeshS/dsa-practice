def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])   # sum of first window
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]        # add new element
        window_sum -= arr[i - k]    # remove old element
        max_sum = max(max_sum, window_sum)

    return max_sum


# Test
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))