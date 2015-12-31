import random as R
import math as M
S = []
num_elements = 1000
max_value = 1000
current = 0

# Return n random ints, no repeats.
def generate_S(num_elements, max_value):
	S = []
	for i in range(0, num_elements):
		rand_num = R.randint(0, max_value)
		while rand_num in S:
			rand_num = R.randint(0,max_value)
		S.append(rand_num)
		print(rand_num)
	return S

# Assumes vectors are equal length
def vector_subtraction(A, B):
	S = []
	for i in range(0, len(A)):
		S.append(A[i] - B[i])
	return S

# Assumes vectors are equal length
def vector_addition(A, B):
	S = []
	for i in range(0, len(A)):
		S.append(A[i] + B[i])
	return S

S = generate_S(num_elements, max_value)
Backup = list(S)

# returns index of S marking the point with the minimum distance
#   from the current point current
def find_closest_point(current, A):
	current_point = A[current]
	A.pop(current)
	min_dist = M.fabs(current_point - A[0])
	min_dist_element = 0
	for i in range(1, len(A)):
		tmp_dist = M.fabs(current_point - A[i])
		if(tmp_dist < min_dist):
			min_dist = tmp_dist
			min_dist_element = i
	return min_dist, S[min_dist_element], min_dist_element

Solution_S = [S[0]]
total_time = 0

print('Starting at point S[0] with value: ' + str(S[0]))
while len(S) > 1:
        message = 'At point '+str(S[current])+'.'
        print(message)
        mdist, Svalue, current = find_closest_point(current, S)
        message = 'Closest value is '+str(mdist)+' units away at point '+str(Svalue)+'.'
        print(message)
        total_time += mdist
        message = 'Total time elapsed is ' + str(total_time)
        Solution_S.append(Svalue)
        print(message)
print('Final point: ' + str(S[0]))

print('Solution S array:')
print(Solution_S)
			
