items = ["a", "b", "c", "d", "e", "f"]
print(items[1:4])    # ['b', 'c', 'd'] (indices 1, 2, 3)
print(items[:2])     # ['a', 'b'] (first two)
print(items[-2:])    # ['e', 'f'] (last two)
print(items[::2])    # ['a', 'c', 'e'] (every second element)
print(items[::-1])   # ['f', 'e', 'd', 'c', 'b', 'a'] (reversed copy)