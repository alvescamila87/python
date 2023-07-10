#orientação a objetos: encapsulamento

class Aviao:

    __asas = 4

    def __init__(self, marca):
        self.marca = marca

    def mostrar_asas(self):
        print("O avião da marca %s tem %d asas." %(self.marca, self.__asas))

aviao = Aviao("Boing")
print(aviao.marca)

#acessar método asa dessa forma, não é possível acessar/imprimir nem modificar valor, pois é um método privado
#print(aviao.__asas)

#jeito certo de acessar, é incluindo o método como uma def e invocar:
aviao.mostrar_asas()