# Pablo Martinez Agullo
# ML Course - Exercises Chapter 1
# 10/03/2019

# Bernstein polynomials



import numpy as np
import matplotlib.pyplot as plt
#import sys 


## 2.1  Plot the n=4 Bernstein polynomials ##

print("Plotting the Bernstein polynomials for n=4")
# The matplotlib function 'plot' takes as an argument two lists of numbers.
x = np.linspace(0,1,100)  # create evenly-spaced points in a given interval
y0 = (1-x)**4						  # Berstein n=4 j=0
y1 = 4*x*(1-x)**3					# Berstein n=4 j=1
y2 = 6*(x**2)*(1-x)**2		# Berstein n=4 j=2
y3 = 4*(x**3)*(1-x)				# Berstein n=4 j=3
y4 = x**4							    # Berstein n=4 j=4

plt.plot(x, y0, '-r', label='B (n=4,j=0)(x)')
plt.plot(x, y1, '-g', label='B (n=4,j=1)(x)')
plt.plot(x, y2, '-b', label='B (n=4,j=2)(x)')
plt.plot(x, y3, '-m', label='B (n=4,j=3)(x)')
plt.plot(x, y4, '-y', label='B (n=4,j=4)(x)')
plt.title('Bernstein polynomial for n=4')
plt.legend(loc='upper right')
plt.grid()
plt.show()
print("\n")
print("\n")


## 2.2 Change the base from B to S ##
# B = (  B(n=4,j=0),B (n=4,j=1),B (n=4,j=2,),B (n=4,j=3),B (n=4,j=4) )  	Berstein polinomial base
# S = (  1, x, x**2, x**3, x**4)											Standard polinomial base

print("Change of base from Berstein polinomial base (B) to Standard polinomial base(S), being:" + "\n" + "B = (  B(n=4,j=0),B (n=4,j=1),B (n=4,j=2,),B (n=4,j=3),B (n=4,j=4) )" + "\n" + "S = (  1, x, x^2, x^3, x^4)")

# if P_SB =( S[0]_B, S[1]_B, S[2]_B, S[3]_B, S[4]_B  )
# 	then for every v in V:
#		[v]_S = P_SB  [v]_B

print("We write the each element of the base B as a vector of the base S:")
print ("S[0]_B = (1, 4, 6, 4, 1)")
print ("S[1]_B = (0, 4, -12, 12, -4)")
print ("S[2]_B = (0, 0, 6, -12, 6)")
print ("S[3]_B = (0, 0, 0, 4, -4)")
print ("S[3]_B = (0, 0, 0, 0, -1)")
print("\n")


P_SB = np.array([[1, 0, 0, 0, 0],[4, 4, 0, 0, 0],[6, -12, 6, 0, 0],[4, 12, -12, 4, 0],[1, -4, 6, -4, 1]])

print("The change of base matrix from S to B, P_SB, is:")
print(P_SB)
print("\n")


Q_BS = np.linalg.inv(P_SB)
print("The change of base matrix from B to S, Q_BS, is:")
print(Q_BS)
print("\n")
print("\n")



## 2.3 Express in the Bernstein base a polinomial which is in the standard base
print("Consider the polynomial p(x) = 3x^4 −8x^3 + 6x^2 −12x+ 4.")
# Using the matrix computation [p(x)]B = Q_BS[p(x)]_S
print("In S this is: (1, -12, 6, -8, 3)")

p_S = np.array([[1],[-12],[6],[-8],[3]])
p_B = np.dot(Q_BS,p_S)

print(p_B)   # <- no me da bien
#print("\b")
#print(np.dot(P_SB,p_B))
