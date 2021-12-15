

class AlunoModel:


    def __init__(self):
        self.__matricula = str
        self.__nome = str
        self.__email = str
        self.__genero = str
        self.__senha = str
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setGenero(self, genero):
        self.__genero = genero
    
    def getGenero(self):
        return self.__genero

    def setSenha(self, senha):
        self.__senha = senha

    def getSenha(self):
        return self.__senha


    def verDados(self):
        data = f"{self.getMatricula()},{self.getNome()},{self.getEmail()},{self.getGenero()},{self.getSenha()}\n"
        #self.getMatricula()+"\n"+self.getNome()+"\n"+self.getEmail()+"\n"+self.getGenero()+"\n"+self.getSenha()+"\n"
        return data

        #return self.getMatricula()+"\n"+self.getNome()+"\n"+self.getEmail()+"\n"+self.getGenero()+"\n"+self.getSenha()

    def Salvar(self):
        arq = open('model/dados.txt','a')
        arq.write(self.verDados())
        arq.close()
        
    def validarGravacao(self):
        arq = open('model/dados.txt','r')
        linhas = arq.readlines()
        result = []
        data = self.verDados()
        for l in linhas:
            result.append(l.replace('\n', ''))
            if data in linhas:
                return print('ok')
            else: 
                return print('não')   
        alunos = []
        for d in result:
            if "," in d:
                individual = d.split(",")
                alunos.append(individual)
        arq.close()
        #return print(alunos,len(alunos))
            
        
        
        
    


