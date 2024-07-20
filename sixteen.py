def swap_keys_and_values(d):
    return {v: k for k, v in d.items()}
d = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", d)
print("Dictionary with Keys and Values Swapped:", swap_keys_and_values(d))
