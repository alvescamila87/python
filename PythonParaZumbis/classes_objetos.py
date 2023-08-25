
# Classe Televisão 1
class Televisao:
    def __int__(self):
        self.ligada = False
        self.canal = 2


tv_quarto = Televisao()
tv_sala = Televisao()
tv_cozinha = Televisao()
tv_quarto.ligada = True
tv_quarto.canal = 5

# Classe Televisão 2

class Televisao:
    def __int__(self):
        self.ligada = False
        self.canal = 2

    def mudar_canal_acima(self):
        self.canal += 1
    def mudar_canal_abaixo(self):
        self.canal -= 1

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 5
tv_sala.mudar_canal_abaixo()
tv_sala.mudar_canal_acima()
