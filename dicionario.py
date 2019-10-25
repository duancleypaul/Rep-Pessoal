marks = {'Rahul' : 86, 'Ravi' : 92, 'Rohit' : 75}
print(marks)
print(marks.keys())
print(marks.values())

# adicionando elementos ao dicionario:
# OBS: para dicionarios nao precisa usar append para adicionar elementos

marks['aa'] = 33
marks['bb'] = 45

for it in marks.items():
	print(it)	# .items() imprime uma dupla (chave e valor)
