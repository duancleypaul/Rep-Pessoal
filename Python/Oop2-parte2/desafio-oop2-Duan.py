from opencage.geocoder import OpenCageGeocode
from ipyleaflet import *
from pprint import pprint

class Biodiversidade_csv:
    def __init__(self, arquivo):
        self.arquivo = list(open(arquivo))      # Abrindo arquivo como lista (cada linha eh uma lista)

    def qtdLinhasDadosFaltantes(self):
        self.lista_faltantes = []
        titulos = self.arquivo[0].split(";")    # titulos = var local do tipo lista, onde cada item eh uma coluna da linha 0
        
        # self.lista_faltantes[0] recebe titulos, mas sem as marcacoes de nova linha '\n'
        # essa linha eh desprezivel, mas se assim fizer, considerar que o indice 0 ja contera dados do arquivo .csv
        [self.lista_faltantes.append([titulos[i].replace('\n',''),0]) for i in range(0,len(titulos))]

        # Este loop conta o numero de informacoes faltantes em cada coluna.
        # O resultado sera uma lista de listas duplas (self.lista_faltantes)
        #   no formato [['Titulo 1', contador de faltantes 1], ['Titulo 2', contador de faltantes 2], ...]
        for i in range(1,len(self.arquivo)):
            linha = self.arquivo[i].split(";")
            for j in range(0,len(linha)):
                if linha[j] == "" or linha[j].lower() == "sem informações":
                    self.lista_faltantes[j][1] += 1
        
        # copiando a lista de faltantes para a variavel local "media"
        media = self.lista_faltantes[:]
        
        print("--- Media de Dados Faltantes por Coluna ---")
        # Descricao do loop abaixo:
        # - Em cada coluna (indice i) da variavel media, o valor do contador (indice 1) receberar o calculo da media da coluna
        # - A funcao round arredonda o resultado para 3 casas decimais
        # - Cada coluna sera impressa com seu respectivo valor de media
        for i in range(0,len(media)):
            media[i][1] = round(media[i][1] / len(self.arquivo[1:]),3)
            print(media[i])
        
        # Apesar do calculo da media, o desafio pede pra que a funcao retorno a quantidade de linhas faltantes por coluna.
        return self.lista_faltantes

    #def nivelTax(self, inicio=1):
    def nivelTax(self):
        print("\n------Nível Taxonômico-----")
        
        self.temp = [linha.strip("\n").split(';') for linha in self.arquivo]     # aloca a taxonomia a ser lida na iteracao       
        self.nvTax = []     # aloca o nivel taxonomico de cada item no formato: 
                            # [['Nivel Taxonomico de 1:','Especie'],['Nivel Taxonomico de 2:','Genero'],...]
       
        for i in range(len(self.arquivo[1:])):
            if self.temp[i][21].lower() != "Sem Informações".lower() and self.temp[i][21] != "":
                self.nvTax.append(["Nível Taxônomico de {}:".format(i),"Espécie"])
            elif self.temp[i][20].lower() != "Sem Informações".lower() and self.temp[i][20] != "":
                self.nvTax.append(["Nível Taxônomico de {}:".format(i),"Gênero"])
            elif self.temp[i][19].lower() != "Sem Informações".lower() and self.temp[i][19] != "":
                self.nvTax.append(["Nível Taxônomico de {}:".format(i),"Família"])
            elif self.temp[i][18].lower() != "Sem Informações".lower() and self.temp[i][18] != "":
                self.nvTax.append(["Nível Taxônomico de {}:".format(i),"Ordem"])
            elif self.temp[i][17].lower() != "Sem Informações".lower() and self.temp[i][17] != "":
                self.nvTax.append(["Nível Taxônomico de {}:".format(i),"Classe"])
            else:
                self.nvTax.append(["Nível Taxônomico de {} :".format(i),"Filo"])
        
        # Usar linhas abaixo para imprimir valores taxonomicos de cada nivel, a titulo de teste
        #for i in self.nvTax[:50]:
        #   print(i)
        
        return self.nvTax

       

    def filtro_ocorrencias(self, categoria, filtro):
        ''' --- DESCRICAO DE USO DO PARAMETRO "filtro" ---
        > A funcao ira retornar os itens que possuem o conteudo do filtro
          em comum.[]
        > Parametro 1: insira o nu[]mero correspondente a categoria desejada
        > Parametro 2: insira o va[]lor correspondente a categoria escolhida
        > Opcoes de filtro:[]
            0- Nome da instituicao[]
            1- Sigla da instituica[]o
            2- Nome da base de dados
            3- Sigla da base de dados
            4- Responsavel pelo registro
            5- Numero do registro no portal
            6- Numero do registro na base de dados	
            7- Data do registro
            8- Data do evento
            9- Data de Carencia
            10- Nome cientifico
            11- Nome comum
            12- Nome cientifico na base de dados
            13- Nivel taxonomico
            14- Numero de individuos
            15- Reino
            16- Filo
            17- Classe
            18- Ordem
            19- Familia
            20- Genero
            21- Especieque 
            22- Estado de conservacao
            23- Categoria de Ameaca
            24- Localidade
            25- Pais
            26- Estado/Provincia
            27- Municipio
            28- Status de Sensibilidade
            29- Latitude
            30- Longitude
            31- Outras informacoes da localidade
            32- Jurisdicao
            33- Destino do Mocorrencia

            Exemplo de uso: ocorrencia
                obj = Biodiversidade_csv()
                obj.filtro_ocorrencias(1,"JBRJ")
                --- OUTPUT:
                    Numero de ocorrencias do filtro: 10
        '''
        self.ocorrencia = []
        for i in range(0,len(self.arquivo[1:])):
            if self.arquivo[i].split(";")[categoria].lower() == filtro.lower():
                self.ocorrencia.append([self.arquivo[i].split(";")]) 
        if len(self.ocorrencia) == 0:
            print("Nao ha ocorrencias do filtro inserido ou a categoria inserida eh invalida.")
        else:       
            print("Numero de ocorrencias do filtro:",len(self.ocorrencia))
        return self.ocorrencia
    
    def checkLatLong(self):
        self.latLong = []       # Lista de listas: cada sublista esta no formato [lat,long]
        self.city = []          # Lista de cidades 
        self.indexNotOK = []
        [self.latLong.append([i.split(";")[29],i.split(";")[30]]) for i in self.arquivo[1:60]]
        [self.city.append(i.split(";")[27]) for i in self.arquivo[1:60]]

        key = 'b3581bc610a644f896bd87fc2cd8e6ce'
        geocoder = OpenCageGeocode(key)
        
        for i in range(0,len(self.latLong)):
            results = geocoder.reverse_geocode(self.latLong[i][0], self.latLong[i][1])
            if  self.city[i].lower() != results[0]['components']['city'].lower():
                #self.notOK.append([["City from geocoder: "+results[0]['components']['city']],["City from csv-file: "+self.city[i]],["Index: "+str(i)]])
                self.indexNotOK.append(i)

        print("Indices dos dados conflitantes:",self.indexNotOK)        
        return self.indexNotOK
        
obj = Biodiversidade_csv("portalbio_export_17-10-2019-13-06-22.csv")
#obj.qtdLinhasDadosFaltantes()                      #OK
obj.nivelTax()
#obj.filtro_ocorrencias(1,"JBRJ")                   #OK
#obj.checkLatLong()                                 #OK (o delay no output eh por causa do acesso a API geocoder)