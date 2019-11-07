def findAnagram(lista):
    anagram = []
    temp = [[i for i in lista if sorted(i) == sorted(j)] for j in lista]
    for i in temp:
        if i not in anagram:
            anagram.append(i)
    return print(anagram)

findAnagram(["eat","ate","done","tea","soup","node"])   
