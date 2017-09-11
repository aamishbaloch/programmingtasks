# In an array with integers between 1 and 1,000,000 one value is in the array twice. How do you determine which one?
def find_duplicate(arr):
    orig_len = len(arr)
    if orig_len <= 1:
        return None
    pivot = arr.pop(0)
    greater = [i for i in arr if i > pivot]
    lesser = [i for i in arr if i < pivot]
    if len(greater) + len(lesser) != orig_len - 1:
        return pivot
    else:
        return find_duplicate(lesser) or find_duplicate(greater)