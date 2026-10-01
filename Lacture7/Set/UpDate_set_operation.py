set1 = {1, 2, 3, 4, 5}
set2 = {4,5,6,7}



set1 &= set2
print("After intersection (set1 &= set2):", set1)

set1 = {1, 2, 3, 4, 5}

set1 -= set2
print("After difference (set1 -= set2):", set1)

set1 = {1, 2, 3, 4, 5}

set1 ^= set2
print("After symmetric difference (set1 ^= set2):", set1)