import calendar
import calendario



class Funcionario:
    def __init__(self, nome: str, ultima_folga: int):
        self.nome = nome
        self.ultima_folga = ultima_folga
        self.lista_fun = []
        print(f'Funcionário(a) {self.nome} Adicionado!')
    

    def exibir_informacoes(self):
        return f'Funcionário: {self.nome} | Última folga: {self.ultima_folga}'
    

    def lista_funcionarios(self):
        
        self.lista_fun.append(self.nome)
        return self.lista_fun























  
    
            
       

    
