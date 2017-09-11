def mergesort(numbers):
    if len(numbers) > 1:
        mid = int(len(numbers) / 2)

        left = numbers[:mid]
        right = numbers[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j <len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            numbers[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            numbers[k] = right[j]
            k += 1
            j += 1
