def mutate(word):
	abc = ["a","b","c","d","e","f",
"g","h","i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x","y","z"]
	# Mutacao 1: Inserindo um caracter
	mutacao1 = [''.join([word[:i], letra, word[i:len(word)]]) for i in range(len(word)+1) for letra in abc]
	# Mutacao 2: Removendo um caracter
	mutacao2 = [''.join([word[:i], word[i+1:len(word)]]) for i in range(0,len(word))]
	# Mutacao 3: Substituindo caracter
	mutacao3 = [''.join([word[:i], letra, word[i+1:len(word)]]) for i in range(len(word)) for letra in abc] 
        # Mutacao 4: Trocando dois caracteres consecutivos
	mutacao4 = [''.join([word[:i],word[i+1],word[i],word[i+2:len(word)]]) for i in range(0,len(word)-1)]
	# Somando tudo numa soh lista
	resultado = mutacao1+mutacao2+mutacao3+mutacao4

	return resultado

''' Testando  funcao
words = mutate("hello")
#print(words)
print("helo" in words)
'''
