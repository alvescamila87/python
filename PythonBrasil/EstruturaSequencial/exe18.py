# Entrada de dados
arquivo = int(input("Informe o tamanho de um arquivo para download (em MB): "))
velocidade = int(input("Informe a velocidade de um link de internet (em Mbps): "))

# Processamento de dados

tempo = arquivo / velocidade
minuto = tempo / 60

# Saída de dados
print(f'O tempo aproximado para download do arquivo usando este link é de: {minuto:.2f} minutos.')