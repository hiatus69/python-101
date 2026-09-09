set_a = {1, 2, 3, 4}
set_b = {2,3}
set_c = {1,2,3,4}
set_d = {1,2,3,4,5}

# superset and subset
print("set_a is superset of set_b:", set_a >= set_b) #supersey
print("set_b is subset of set_a:", set_b <= set_a) #subset

# Proper Superset and Proper Subset
print("set_a is proper superset of set_c:", set_a > set_b) #True proper superset
print("set_a is proper superset of set_c:", set_a > set_c) #False proper superset
print("set_b is proper subset of set_a:", set_b < set_a) #True proper subset

# equal sets
print("set_a is equal to set_c:", set_a == set_c) #True equal sets

print("set_b is proper subset of set_d: and not equal:", set_b <= set_d and set_b != set_d) #True proper subset