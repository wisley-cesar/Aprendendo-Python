# Aula 07 de 34:
# O que é o self das Classes

# classe
class TV:
    # vamo criar uma função que chamos de método dentro da classe
    # método inicial
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10

    def liga_tv(self):
        self.ligada = True

    def aumentar_colume(volume): # um exemplo com mundando o nome do self para volume
        volume.volume +=1



# Programa
tv_sala = TV()
tv_sala.liga_tv()
tv_sala.aumentar_colume()
print(tv_sala.volume)
print(tv_sala.cor)
print(tv_sala.ligada)


# Vamos aprender para que serve o "self" que é passado como parametro dentro da função __init__
# O self é passado dentro dos () por que ele sempre tem que ser o primeiro parametro,
# quando você criar um metodo(função) o proprio pycharm vai completar com o self para você, ele é obrigatorio, mas ele
# nao precisa nessariamente se chamar self, Na verdade todo metodo em python tem que passar um parametro, seja ele qual
#  for o nome, entao para acessar um atributo da classe temos que colocar um parametro

