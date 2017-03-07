import math

def cosine_similarity(vector_a, vector_b, vector_dot):
	a_vector_magnitude = 0
	for elem in vector_a:
		a_vector_magnitude += math.pow(elem, 2)
	b_vector_magnitude = 0	
	for elem in vector_b:
		b_vector_magnitude += math.pow(elem, 2)

	magnitude = math.sqrt(a_vector_magnitude) * math.sqrt(b_vector_magnitude)
	dot_product = 0
	for d in vector_dot:
		dot_product += d
	
	return dot_product / magnitude
