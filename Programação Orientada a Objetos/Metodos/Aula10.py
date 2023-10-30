#Aula 10 de 34: Parâmetros no init da Classe
class TV:

# Passando paremetro na função init

    def __init__(self, tamanho):
        self.cor = 'preta'
        self.ligada  = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10


    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
# agora para criar um tv é obrigatorio passar o tamannho dela
# voce pode passar de dois jeitos os parametros
# primeiro jeito mais intuitivo

tv_sala = TV(tamanho = 55)
tv_quarto = TV(tamanho = 65)

print(tv_sala.tamanho, tv_quarto.tamanho)
# segundo jeito menos intuitivo

tv_sala = TV(99)
tv_quarto = TV(100)

# ambos fazem a mesma coisa
print(tv_sala.tamanho, tv_quarto.tamanho)