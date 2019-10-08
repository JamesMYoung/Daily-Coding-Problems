# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Stripe.
# 
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# 
# You can modify the input array in-place.

# Had to look up the answer for this problem
# However, did learn interesting concepts:
# - Segregation of an array, in linear time
#   as well as the relative power of such an
#   operation

def find_lowest_pos_int(Arr):
	hold = 0
	
	print(Arr)
	Arr, j = seg_arr(Arr)
	print(Arr)
	
	Arr = Arr[j:]
	print(Arr)
	return find_missing_pos(Arr)
	
		
# Move negative numbers to left, pos to right
def seg_arr(Arr):
	j = 0
	for i in range(len(Arr)):
		if Arr[i] < 0:
			Arr[j], Arr[i] = Arr[i], Arr[j]
			j += 1
			
	return Arr, j
	
def find_missing_pos(Arr):

	for i in range(len(Arr)):
		if abs(Arr[i])-1 < len(Arr) and Arr[abs(Arr[i])-1] > 0:
			Arr[abs(Arr[i]) - 1] = -1 * Arr[abs(Arr[i]) - 1]
		print(i, ":", Arr)
	
	for i in range(len(Arr)):
		if Arr[i] > 0:
			print("returning i+1")
			return i+1
			
	return len(Arr) + 1
	
	
input1 = [12, 32, 24, 6, 1, 2, 3, -10, -20]

a = find_lowest_pos_int(input1)


print(a)






