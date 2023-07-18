from conta import Conta, Cliente

cliente1 = Cliente("Camila", "Jesus", "111111111-22")
cliente2 = Cliente("Karoline", "Jesus", "999999999-66")


conta1 = Conta("5555-7", cliente1, 5000, 7000)
conta2 = Conta("8888-4", cliente2, 300, 1000)

conta1.depositar(500)
conta1.sacar(20)
conta1.extrato()
conta1.transferir_para(conta2, 400)
conta2.extrato()

cliente3 = Cliente("Paulo", "Jesus", "666666666-77")
conta3 = Conta("741-8", cliente3, 100, 300)
conta3.depositar(1000)
conta3.historico.imprimir()

