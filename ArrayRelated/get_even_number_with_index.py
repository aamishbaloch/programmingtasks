def get_even_number_with_even_index(numbers):
    return [x for index, x in enumerate(numbers) if (x % 2 == 0 and index % 2 == 0)]


print(get_even_number_with_even_index([2, 3, 5, 4, 4]))
