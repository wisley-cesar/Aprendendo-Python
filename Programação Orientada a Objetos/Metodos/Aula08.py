# Aula 08 de 34:
# Criando Métodos dentro das Classes

class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10
        # como criar um método em python
        # todo método tem () 
    def mudar_canal(self):
        self.canal = 'Disney+'


tv_sala = TV()
tv_sala.mudar_canal()
tv_quarto = TV()


print(tv_sala.canal)
print(f'A tv do quarto esta no canal da {tv_quarto.canal} e a tv da sala está no canal {tv_sala.canal}')