numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

#print square(5)			#python2
#print square(2*5)			#python3

print(square(5))		# Multiplicacoes executadas: 1
print(square(2*5))		# Multiplicacoes executadas: 2
