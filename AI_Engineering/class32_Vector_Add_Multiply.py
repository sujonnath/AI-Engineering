#Vector Addition and Multiplication
import numpy as np

vector_p = np.array([1,3])
vector_q = np.array([5,9])
sum_vector = vector_p+vector_q
multiplication_of_vector = vector_p*vector_q
#print(type(b))
print("Sum:",sum_vector) #sum = [1+5 3+9]
print("Multiplication:",multiplication_of_vector) # multiplication_of_vector = [1*5 3*9]

#Dot Product
v1 = np.array([1,3,9])
v2 = np.array([2,7,10])

dot = np.dot(v1,v2)
print("Dot Product:", dot) # dot= (1*2+3*7+9*10)

A = np.array([
    [1,2],
    [3,4]
])
B = np.array([
    [5,6],
    [7,8]
])

result = np.dot(A,B)
print(result) # [[1*5+2*7  1*6+2*8]  [3*5+4*7  3*6+4*8]]