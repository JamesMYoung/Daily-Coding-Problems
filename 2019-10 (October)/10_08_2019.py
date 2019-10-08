# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Jane Street.
# 
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# 
# Given this implementation of cons:
# 
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# 
# Implement car and cdr.

# A solution was looked up
# Interesting aspects here;
# This is an example of functional programming,
# using functions to achieve the results, rather
# than using data structures (such as lists)

def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair
	
def car(f):
	def left(a, b):
		return a
	return f(left)
	
def cdr(f):
	def right(a, b):
		return b
	return f(right)
	

print(type(cons(1, 2)))
print(car(cons(3, 5)))
print(cdr(cons(2, 9)))