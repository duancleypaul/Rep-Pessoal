
import copy

vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels)

lista = vowels

print(lista)
lista[1]='z'

print(lista)
print(vowels)

lista_2D = [[1, 3, 2, 10],[1.2, -0.2, 0, 2]]
c = copy.deepcopy(lista_2D)
c[0][0] = 'a'

print(c)
print(lista_2D)

books = []
books.append('teste')
print(books)

books.append('abc')
print(books)

#del books[1]		# deleta elemento [1] da lista books
#print(books)

books.sort()
print(books)
