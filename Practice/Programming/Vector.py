#first method
v1 = list(map(int,input("Enter number for vector with space:").split()))
v2 = list(map(int,input("Enter number for vector with space:").split()))
result = []
for i in range(len(v1)):
    result.append(v1[i]*v2[i])
print(result)
#second method by numpy
print("________________________________")
import numpy as np
v1 = np.array(list(map(int,input("Enter a number for vector with space:").split())))
v2 = np.array(list(map(int,input("Enter a number for vector with space:").split())))
print(v1*v2)