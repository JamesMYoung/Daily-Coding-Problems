# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Uber.
# 
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# 
# Follow-up: what if you can't use division?

# bit of a rough function name
def new_prod_arr_sans_i(L):
	new_L = []
	for i in range(len(L)):
		# start with 1 for product
		hold_num = 1
		for j in range(len(L)):
			if i != j:
				hold_num *= L[j]
			
		new_L.append(hold_num)
	return new_L
	
L = [1, 2, 3, 4, 5]

L2 = new_prod_arr_sans_i(L)

print(L2)