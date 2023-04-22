// Manipulating text

cadeia de texto:
'Curso em video python'

fatiamento
frase[9]
frase[:13] sem indicação de início
frase[13:] sem indicação de final
frase[1:14:2] pula os caracteres de 2 em 2
frase[1::2] pula os caracteres de 2 em 2, sem indicação de final
frase[::2] pula os caracteres de 2 em 2, sem indicação início e fim

análise
- len(): ver tamanho da string
- .count('o',0,13)
- .find('deo'): procurar
    se receber '-1' = não encontrado
    - 'curso' in frase

transformação
- .replace('python', 'android')
- .upper()
- .lower()
- .capitalize()
- .title(): ~capitalize
- .strip(): remover espaços ínúteis no começo e no final da string
    - .rstrip(): remove espaços só da direita
    - .lstrip(): remove espaços só da esquerda

divisão
- .split(): divisão dos espços, divisão de string em uma lista

junção
- '-'.join(): gera string única separado por '-', pode deixar ' ' para colocar espaço

texto longo
- print("""texto longo, texto longo, texto longo, texto longo, texto longo, texto longo, texto longo, texto longo, texto longo, texto longo, """)