# Aula 06 de 34:
#Criando nossa 1ª Classe


# Criando nossa 1 Classe em python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe(object):
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse mmétodo é quem define o que acontece quando você cria uma instância da Classe

# Vamos fazer um exemplo para facar mais claro, como o caso da televisão que a gente vinha comentando


class TV:
    # vamo criar uma função que chamos de método dentro da classe
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10



tv_sala = TV()
tv_quarto = TV()

print(tv_sala.cor)
print(tv_sala.canal)
tv_quarto.tamanho = 75
print(tv_sala.tamanho)
print(tv_quarto.tamanho)
print(tv_quarto.volume)


print(tv_quarto.volume)





