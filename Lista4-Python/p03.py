import math

def checkSpeed(speed):
	points = 0
	if speed <= 70:
		print("Ok")
		return points
	else:
		points = math.ceil((speed-70)/5)
		if points <= 12:
			print("Total of demerit poits: ",points)
			return points
		else:
			print("License suspended.")
			return points

#checkSpeed(80)		# testando a funcao
