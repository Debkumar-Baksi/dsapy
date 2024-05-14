class sort:
    def bubble_sort(arr):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x <= pivot]
            right = [x for x in arr[1:] if x > pivot]
            return sort.quick_sort(left) + [pivot] + sort.quick_sort(right)
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  
            left_half = arr[:mid]  
            right_half = arr[mid:]
            sort.merge_sort(left_half) 
            sort.merge_sort(right_half) 
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)
        return arr
    def radix_sort(arr):
        max_num = max(arr)
        max_digit = len(str(max_num))
        for digit in range(max_digit):
            buckets = [[] for _ in range(10)]
            for num in arr:
                digit_val = (num // 10 ** digit) % 10
                buckets[digit_val].append(num)
            arr = [num for bucket in buckets for num in bucket]
        return arr

# END OF SORTING #