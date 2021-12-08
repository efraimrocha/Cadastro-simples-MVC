from model.alunoModel import AlunoModel

class AlunoController:

    def __init__(self):
        pass

    def pegarDados(self, janTkfull):
        matricula = janTkfull.getTexto(4)
        nome = janTkfull.getTexto(6)
        email = janTkfull.getTexto(8)
        genero = janTkfull.getTexto(10)
        senha = janTkfull.getTexto(12)
        
        aluno = AlunoModel()
        aluno.setMatricula(matricula)
        aluno.setNome(nome)
        aluno.setEmail(email)
        aluno.setGenero(genero)
        aluno.setSenha(senha)
        return aluno.verDados()

    def gravarDados(self):
        self.gravar=AlunoModel()
        self.gravar.inserirDados()
