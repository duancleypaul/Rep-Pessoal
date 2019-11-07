x = 1
def f():
	x = 2
	return x
#print x			#python2
#print f()			#python2
#print x			#python2

print(x)			#python3
print(f())			#python3
print(x)			#python3

# Output:
# 1
# 2
# 1
