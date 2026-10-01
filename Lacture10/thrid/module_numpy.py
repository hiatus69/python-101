import numpy as np

random_matrix = np.random.randint(1, 11, size=(3,3))
print("random 3x3 Matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print("\n Sum of all elements: ", matrix_sum)

matrix_mean = np.mean(random_matrix)
print("\n Mean of matrix: ", matrix_mean)

transposed_matrix = np.transpose(random_matrix)
print("\nTramsposed Matrix:\n",transposed_matrix)