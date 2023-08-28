# Live #34 - Trabalhando com arquivos de texto - Buffering
# tamanho que será ocupado em memória durante a leitura (chunks)
# mode, buffering, enconding, errors, newline, closefd, opener

import os
print(os.stat('teste_buffering.txt').st_blksize)

import io
print(io.DEFAULT_BUFFER_SIZE)

