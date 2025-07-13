import numpy as np

v = np.array([3,4])
print("Vector:", v)

Vector_example=[
    [7,11,56,89],
    [8,6],
    [2,4],
    [10,4,6,9,0],
    [1]
]

Vector_example1=[
    [7,11],
    [8,6],
    [2,4],
    [10,4],
    [1,9]
]

print("Vector:", Vector_example)
print("Length of outer list:", len(Vector_example))
print("Length of each sub-list:", [len(sublist) for  sublist in Vector_example])

arr = np.array(Vector_example, dtype=object)
print("Array Shape:", arr.shape)

arr1 = np.array(Vector_example1, dtype=object)
print("Array Shape:", arr1.shape)

shape_of_vector_example= np.shape(Vector_example1)
print(shape_of_vector_example)

