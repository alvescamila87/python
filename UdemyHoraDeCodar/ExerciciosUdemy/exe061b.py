#classe: carro ligado, dirige + velocidade

class Carro:
    velocidade = 0
    ligado = False

    def __init__(self, modelo, tanque):
        self.modelo = modelo
        self.tanque = tanque

    def ligar(self):
        self.ligado = True
        print("Carro LIGADO!")

    def aumentar_velocidade(self, delta, km):
        if self.ligado:
            self.velocidade = self.velocidade + delta
            print("Vrummmmm!")
            km_por_litro = 10
            self.tanque = self.tanque - (km / km_por_litro)
            print("Velocidade %d km/h. Checar nível de garolina!" %delta)
            print("Você percorreu até agora %d km(s). Nível de gasolina: %d lt(s)" %(km, self.tanque))
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
        else:
            self.ligado = False
            print("Carro DESLIGADO!")


fusca = Carro("Fusca", 50)
print(fusca.modelo, fusca.tanque)

fusca.ligar()

fusca.aumentar_velocidade(60, 15)

fusca.desligar()

