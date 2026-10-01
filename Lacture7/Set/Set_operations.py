set1 = {1, 2, 3}
set2 = {3, 4, 5,'apple'}

# Union of two sets
print("Union:", set1.union(set2))
print("Union:", set1 | set2)  # Using the | operator for union
# Intersection of two sets
print("Intersection:", set1.intersection(set2))
print("Intersection:", set1 & set2)  # Using the & operator for intersection
# Difference of two sets
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2 - set1)  # Using the - operator for difference
# Symmetric difference of two sets
print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Symmetric Difference:", set1^set2)  # Using the ^ operator for symmetric difference
