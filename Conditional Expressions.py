scores = [52, 88, 74, 41, 95]
status = ["Pass" if s >= 60 else "Retry" for s in scores]
print(status)  # ['Retry', 'Pass', 'Pass', 'Retry', 'Pass']