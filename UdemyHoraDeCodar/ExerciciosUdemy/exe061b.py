#classe: carro ligado, dirige + velocidade

class Carro:
    velocidade = 0
    ligado = False

    def __init__(self, modelo, tanque):
        self.modelo = modelo
        self.tanque = tanque

    def ligar(self):
        if self.tanque != 0:
            self.ligado = True
            print("Carro LIGADO!")
        else:
            print("Precisa abastecer para ligar o veículo!")

    def aumentar_velocidade(self, delta, km):
        if self.ligado and self.tanque > 2:
            self.velocidade = self.velocidade + delta
            print("Vrummmmm!")
            km_por_litro = 10
            self.tanque = self.tanque - (km / km_por_litro)
            print("Velocidade %d km/h. Checar nível de garolina!" %delta)
            print("Percorrendo %d km(s). Nível de gasolina: %d lt(s)" %(km, self.tanque))
        elif self.ligado and self.tanque > 1:
            print("Abastecer veículo: URGENTE!!!")
        else:
            print("Ligue o motor para dirigir o veículo")

    def abastecer(self, litros):
        if self.tanque >= 100:
            print("Tanque cheio %d lt(s)" %self.tanque)
        else:
            self.tanque = self.tanque + litros
            if self.tanque > 100:
                self.tanque = 0

    def desligar(self):
        if self.ligado:
            if self.velocidade != 0:
                print("Carro em movimento... pare o veículo para desligar o motor.")
            elif self.velocidade == 0:
                self.ligado = False
                print("Carro DESLIGADO!")
        else:
            self.ligado = False
            print("Carro DESLIGADO!")


fusca = Carro("Fusca", 2)
print(fusca.modelo, fusca.tanque)

fusca.ligar()

fusca.aumentar_velocidade(60, 15)

fusca.abastecer(20)
print(fusca.modelo, fusca.tanque)

fusca.aumentar_velocidade(60, 30)

fusca.aumentar_velocidade(0, 0)
print(fusca.modelo, fusca.tanque)

fusca.desligar()

fusca = Carro("Fusca", 0)
print(fusca.tanque)





