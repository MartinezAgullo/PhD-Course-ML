# Pablo Martinez Agullo
# ML Course - Exercises Chapter 1
# 10/03/2019


# Fibonacci with matrices


import numpy as np
#import sys 


##### 1.1

A = np.array([[1, 1],[1,0]]) # Matrix
v_0 = [[1],[0]] # Initial values

print("The Fibonacci matrix is:")
print(A)
print("\n The seeds (1st and 2nd elements) for the Fibonacci secuence are: " +  str(v_0))

k = 7 # We calculate the k+2 element

#A_k = pow(k,A) #pow command is not doing what was suposed

###  Matrix multiplication
#A_k = A
#i=0
#while i < k-1:
#	A_k = np.dot(A_k, A)
#	i = i+1
########

A_k = np.linalg.matrix_power(A, k) #using numpy's linalg

print("A^k = ")
print(str(A_k))

v_k = np.dot(A_k,v_0)

print("\n")
print("The "+str(k+2)+"th element of the Fibonacci serie is: " + str(v_k[0][0]))
print(v_k)
print("\n" +"\n"+ "########")


##### 1.2
# A = P . D . inv(P)
# A^k = P . D^k . inv(P)

Eigen_values = np.linalg.eig(A)[0]
Eigen_vectors = np.linalg.eig(A)[1] #This is also the P matrix
P_inversed = np.linalg.inv(Eigen_vectors)
D = np.array([[Eigen_values[0], 0],[0,Eigen_values[1]]]) # Diagonal Matrix
print("A=PDP^(-1)")
print("Eigen values =" + "\n" + str(Eigen_values))
#print("Eigen vectors =" + "\n" + str(Eigen_vectors[0])+ "\n" + str(Eigen_vectors[1]))
print("P matrix =" + "\n" + str(Eigen_vectors))
print("\n"+"Diagonal matrix D")
print(D)

print("\n" + "A^k = PD^(k) P^(-1)")
D_k = np.linalg.matrix_power(D, k)
A_k_prime = np.dot(Eigen_vectors,np.dot(D_k,P_inversed))
print("Computed with diagonalization A_k=")
print(A_k_prime)
print("\n")
#TestOfA = np.dot(Eigen_vectors,np.dot(D,P_inversed))
#print(TestOfA) 
v_k_prime= np.dot(A_k_prime,v_0)
print(v_k_prime)
