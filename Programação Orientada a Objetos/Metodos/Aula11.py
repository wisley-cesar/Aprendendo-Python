class TV:
    cor = "preta"
    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10


    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = TV(55)
tv_qurto = TV(70)

tv_sala.mudar_canal('Gloobo')

print(tv_qurto.tamanho)
print(tv_sala.cor)
print(tv_qurto.cor)

# não é muito usado esse metodo de mudar a cor da clase ou mudar o atributo da classe.
# Se você colocar a cor como atributo da classe, quando você mnudar ela não vai mudar
# a cor de uma tv vai mudar a cor de todas as tvs
# diferente de mudar a cor quando ela ta na funcão init

TV.cor = "branca"

print(tv_qurto.tamanho)
print(tv_sala.cor)
print(tv_qurto.cor)