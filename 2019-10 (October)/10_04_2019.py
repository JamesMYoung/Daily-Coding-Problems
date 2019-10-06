# Good morning! Here's your coding interview problem for today.
# 
# This problem was recently asked by Google.
# 
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# 
# Bonus: Can you do this in one pass?

def sum_to_k(k, L):
	for i in range(len(L)):
		for j in range(i, len(L)):
			if L[i] + L[j] == k:
				print("Succesfully found k")
				return True
				
	print("did not find k")
	return False

	
L = [1, 2, 3, 4, 5]
L2 = [10, 15, 3, 7]
sum_to_k(6, L)
sum_to_k(20, L)

sum_to_k(17, L2)
