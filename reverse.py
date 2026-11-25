scores = [72, 95, 60, 88]
scores.append(91)
scores.extend([79, 84])
scores.sort(reverse=True)  # Mutates `scores` in place
print(scores)              # [95, 91, 88, 84, 79, 72, 60]

