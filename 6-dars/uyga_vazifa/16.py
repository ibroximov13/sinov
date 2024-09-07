lst = [0, 1, -5, 5, -5]
negatives = [x for x in lst if x < 0]
positives = [x for x in lst if x > 0]
zeros = [x for x in lst if x == 0]

result = negatives + zeros + positives
print(result)
