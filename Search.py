class search:
    def binary_search(arr,target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    def linear_search(arr,target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    def jump_search(arr,target):
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n) - 1] < target:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1
        while arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev] == target:
            return prev
        return -1
    def interpolation_search(arr,target):
        low = 0
        high = len(arr) - 1
        while low <= high and arr[low] <= target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    return low
                return -1
            pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        return -1
    def exponential_search(arr,target):
        def binary_search(arr, target, low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        n = len(arr)
        if arr[0] == target:
            return 0
        i = 1
        while i < n and arr[i] <= target:
            i *= 2
        return binary_search(arr, target, i // 2, min(i, n - 1))
    def fibonacci_search(arr,target):
        n = len(arr)
        fib_m_minus_2 = 0
        fib_m_minus_1 = 1
        fib = fib_m_minus_1 + fib_m_minus_2
        while fib < n:
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib
            fib = fib_m_minus_1 + fib_m_minus_2
        offset = -1
        while fib > 1:
            i = min(offset + fib_m_minus_2, n - 1)
            if arr[i] < target:
                fib = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib - fib_m_minus_1
                offset = i
            elif arr[i] > target:
                fib = fib_m_minus_2
                fib_m_minus_1 -= fib_m_minus_2
                fib_m_minus_2 = fib - fib_m_minus_1
            else:
                return i
        if offset+1<n and arr[offset + 1] == target:
            return offset + 1
        return -1
    def ternary_search(arr,target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            if arr[mid1] == target:
                return mid1
            elif arr[mid2] == target:
                return mid2
            elif target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        return -1

# END OF SEARCHING #