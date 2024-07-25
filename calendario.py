import calendar
from datetime import datetime






class Calendario:
    def __init__(self, ano, mes, ultima_folga: int):
        self.ano = ano
        self.mes = mes
        self.mes_anterior = [[]]
        self.dados_mes = calendar.monthcalendar(self.ano, self.mes)
        self.dias_mes = []
        self.ultima_folga = ultima_folga
        self.dias_folga = []
     
      
        self.retira_zero()
        self.busca_mes_anterior()
        self.mescla_lista()
        self.verifica_dia_mes_anterior()
        self.gera_folga()
      
    
    def busca_mes_anterior(self):

        anterior = calendar.monthcalendar(self.ano, self.mes-1)

        for i in anterior[3:4]:
            if i != 0:
                self.mes_anterior[0].append(i)
                
            
                
        print(f'O mês anterior é: {calendar.month_name[self.mes-1]}\n') 
        


    def verifica_dia_semana(self, d):
                
          
        return calendar.day_name[d]
           
            
        

    def retira_zero(self):
        contador = 0
        while contador <= 5:
            for n in range(5):
                for i in self.dados_mes[n]:
                    if i != 0:
                        self.dias_mes.append(i)
                        contador += 1

    
 

    def mescla_lista(self):
        return self.mes_anterior.extend(self.dias_mes)
    

    def verifica_dia_mes_anterior(self):
        for dia in self.mes_anterior:
            if isinstance(dia, list):
                for d in dia:
                    if d == self.ultima_folga and d in self.mes_anterior[0] and self.mes_anterior.count(d) <= 2:
                        indice = dia.index(d)
                        dia = dia[indice-1 + 1:]
                        for i in dia:
                            if isinstance(dia, list):
                                self.dias_folga.append(i)
                    
                        
                 
            else:
                self.dias_folga.append(dia)

               
         
                    
                

                    
       

            
        
                


    def gera_folga(self):
        'nova_lista = [self.dias_folga[i] for i in range(0, len(self.dias_folga), 6)]'
        'print(nova_lista)'


        print(f'Os próximo dias de folga do funcionário serão:')
        print(self.dias_folga[6::6])
               
                            

            

a = Calendario(2024, 8, 24)

print(a.dias_folga)
        
























