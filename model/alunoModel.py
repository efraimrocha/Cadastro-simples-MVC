

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

    def gravarDados(self):
        pass

    def verDados(self):
        dada = [self.getMatricula(),self.getNome(),self.getEmail(),self.getGenero(),self.getSenha()]
        return dada

        return self.getMatricula()+"\n"+self.getNome()+"\n"+self.getEmail()+"\n"+self.getGenero()+"\n"+self.getSenha()

    # def tratarDados(self):
    #     self.d = self.verDados()
    #     self.dtratado = [d.replace()]

    def inserirDados(self):
        d=[self.verDados()]
        try:
            arq = open("F:/DAD\Atividade 2 - final - cadastro Tkfull\MVC - DAD/model/dados.txt","a+")
            arq.write(d)
            arq.close()
        except:
            open("F:/DAD\Atividade 2 - final - cadastro Tkfull\MVC - DAD/model/dados.txt","a+")

        

    def dadoAluno(self, nome):
        # arq = open('database/dados.txt', "r")
        # linhas = arq.readlines()
        linhas = self.verDados()
        result = []
        dadoaluno = []
        for l in linhas:
            result.append(l.replace('\n', ''))
        for d in result:
            if "," in d:
                aluno = d.split(",")
                dadoaluno.append(aluno)
        return dadoaluno

    def obtemParticipantes(dados):
        participantes = []
        for d in dados:
            if "," in d:
                individual = d.split(",")
                participantes.append(individual)
        return participantes

    #-----------------------------------------------------------
    # entrada = lerArquivo("dados.txt")
    # dados = obtemParticipantes(entrada)
