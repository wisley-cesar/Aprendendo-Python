# Aula 9 de 34:
# Parâmetros nos Métodos das Classes
class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'

# Criando um método com parametro
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f'Canal aleterado para {novo_canal}')
# toda vez que quisermos mudar o canal da tv, vamos poder escolher qual canal queremos colocar agora
# batas colocar o nome da tv EX:(tv_quarto) .mudar_canal e passara o canal que você desseja ou melhor passar o parametro

tv_sala = TV()
tv_quarto = TV()

tv_sala.mudar_canal('Globo')
tv_quarto.mudar_canal('YouTube')
# desse jeito que fica o canal como o parametro
print(tv_sala.canal)
print(tv_quarto.canal)