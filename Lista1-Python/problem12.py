def count_digits(num):
	if(type(num)!=type(1)):
		print("Seu input nao eh inteiro")
	else:
		i=0
		while num>=1:
			num = num/10
			i+=1
		return print(i)

count_digits(123456789)
