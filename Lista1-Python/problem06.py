a, b = 2, 3
c, b = a, c + 1
#print a, b, c			#python2
print(a, b, c)			#python3

# Output: 
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
'''
# A linha "c, b = a, c + 1" possui um erro.
# A variavel c recebe o valor de a (que eh 2),
# mas como a variavel b, na mesma linha, recebe 
# o valor de c+1, o python acusa um erro de 
# declaracao da variavel c, que recebe um valor
# na mesma linha. Para resolver o problema,
# a variavel c deve receber um valor antes de 
# ser usada por outra variavel.
