x = 1
def f():
	#global x		# inicial globalmente x para remover erro
	y = x
	x = 2
	return x + y
#print x			#python2
#print f()			#python2
#print x			#python2

print(x)			#python3
print(f())			#python3
print(x)			#python3

# Output:
'''
1
Traceback (most recent call last):
  File "problem10.py", line 11, in <module>
    print(f())			#python3
  File "problem10.py", line 3, in f
    y = x
'''
# A variavel x nao esta inicializada globalmente dentro da funcao.
# Dessa forma, a funcao f() nao consegue utiliza-la
