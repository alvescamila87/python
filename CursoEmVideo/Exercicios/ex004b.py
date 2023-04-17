identifyAllTypes=input('Type something:')
print('O tipo primitivo desse valor é', type(identifyAllTypes)),
print('Só tem espaços?', identifyAllTypes.isspace()),
print('É um número?', identifyAllTypes.isnumeric()),
print('É alfabético?', identifyAllTypes.isalpha()),
print('É alfanumérico?', identifyAllTypes.isalnum()),
print('Está em maiúsculo?', identifyAllTypes.isupper()),
print('Está em minúsculo?', identifyAllTypes.islower()),
print('Está capitalizada?', identifyAllTypes.istitle()),