import math
C = 50
H = 30

def calculate_Q (D):
	return math.sqrtt((2 * C * D) / H )
	D = float(input("Enter value of D: "))
	Q = calculate_Q (D)
	print("The Value of D: ", Q)
