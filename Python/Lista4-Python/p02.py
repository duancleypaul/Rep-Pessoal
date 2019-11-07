def fizz_buzz(num):
	if num%3==0 and not num%5==0:
		result = "Fizz"
		return result
	elif num%5==0 and not num%3==0:
		result = "Buzz"
		return result
	elif num%3==0 and num%5==0:
		result = "FizzBuzz"
		return result
	else:
		return num

# print(fizz_buzz(2))		# testando a funcao

