import textdistance

class Texto:

    __stopWords = ["the","and","to","that"]

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
    
    def textoLista(self):
        self.listaTexto = [word.lower() for i in open(self.nome_arquivo).readlines() for word in i.split()]
        return self.listaTexto
    
    def cadaPalavraUmaVez(self):
        self.palavrasUmaVez = []
        [self.palavrasUmaVez.append(i) for i in self.textoLista() if i not in self.palavrasUmaVez]
        [print(i) for i in self.palavrasUmaVez]
        return self.palavrasUmaVez

    def wordFrequency(self):
        self.listaTexto = self.textoLista()
        self.frequenciaDict = dict()
        for i in self.listaTexto:
            i = i.strip(",.!?;:")
            if i in self.frequenciaDict:
                self.frequenciaDict[i] += 1
            else:
                self.frequenciaDict[i] = 1
        return self.frequenciaDict

    def top10(self):
        self.sortedFreq = sorted(self.wordFrequency().items(), key = lambda x: x[1])
        self.top10freq = []
        if len(self.sortedFreq) <=10:
            print("Top-(x<10) palavras mais frequentes:")
            for i in range(len(self.sortedFreq),0,-1):
                self.top10freq.append(self.sortedFreq[i])
        else:
            print("\n> Top10 palavras mais frequentes:")
            for i in range(len(self.sortedFreq)-1,len(self.sortedFreq)-11,-1):
                self.top10freq.append(self.sortedFreq[i])
        return self.top10freq

    def med_devp_freq(self):
        self.med_devp = self.wordFrequency()
        print(type(self.med_devp))
        soma = var = 0
        for i in self.med_devp.values():
            soma += i
        self.media = soma/len(self.med_devp.values())
        for i in self.med_devp.values():
            var += (i-self.media)**2
        var /= len(self.med_devp.values())
        self.devP = var**(0.5)
        print("----- Dados Estatisticos -----")
        print("Frequencia media:", round(self.media,3))
        #print("Variancia:", round(var,3))
        print("Desvio Padrao:",round(self.devP,3))
        return self.media, self.devP
        #lista_dict = dict()

    def addStopWord(self, word):
        if word not in self.__stopWords:
            self.__stopWords.append(word)
            return True
        else:
            return True

    def semStopWords(self):
        self.textoSemSW = [i for i in open(self.nome_arquivo).readlines()]
        for i in range(0,len(self.textoSemSW)):
            for j in self.__stopWords:
                if j in self.textoSemSW[i]:
                    self.textoSemSW[i] = self.textoSemSW[i].replace(j,"")
        a = open("arqSemStopWords.txt","w")
        a.writelines("".join(self.textoSemSW))
        return self.textoSemSW
        
    def distanceHamming(self, p1, p2):
        self.distancia = textdistance.hamming.normalized_similarity(p1,p2)
        print("Grau de similaridade:",str(round(self.distancia*100,2))+'%')
        return self.distancia


#//--------------- Linhas de Teste ---------------//
#texto = Texto("she.txt")
#print(texto.textoLista())                      #OK
#print(texto.cadaPalavraUmaVez())               #OK
#print(texto.wordFrequency())                   #OK
#print(texto.top10())                           #OK
#texto.med_devp_freq()                          #OK
#texto.semStopWords()                           #OK
#texto.distanceHamming("abobora","ababora")     #OK


