from view.Tkfull import Janela
from time import sleep, time
from controller.alunoController import AlunoController

class AlunoView:

        vetor=[[' ','CADASTRO DE ALUNO'],
                ['Matrícula',input],
                ['Nome',input],
                ['E-mail',input],
                ['Gênero',('Feminino','Masculino')],
                ['Senha',complex],
                [{'*Sair':''},' ',{'*Cadastrar':''}]
                ]

        def __init__(self):
                self.jan = Janela()
                self.jan.gerar(self.vetor)
                self.jan.setEvento(15,self.Cadastrar)
                self.jan.setEvento(13,self.Sair)
                self.jan.start()


        def Sair(self):
                msn = "O programa será emcerrado"
                self.jan.mensagem(msn)
                sleep(1)
                quit()

        def Cadastrar(self):         
                dados = AlunoController()
                valid = dados.validacao()
                dados = dados.pegarDados(self.jan)               
                self.jan.mensagem("Dados gravados com sucesso!")
                print(valid)
        
       

