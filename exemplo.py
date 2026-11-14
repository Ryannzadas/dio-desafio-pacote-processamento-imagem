"""Exemplo de uso do pacote com uma imagem que já vem no scikit-image.

Gera os arquivos de resultado na pasta exemplos/.
"""

import os

from skimage import data

from processamento_imagem.processamento import (
    binarizar_imagem,
    converter_para_cinza,
    encontrar_diferenca,
    redimensionar_imagem,
    transferir_histograma,
)
from processamento_imagem.utilidades import salvar_imagem

os.makedirs("exemplos", exist_ok=True)
original = data.astronaut()
referencia = data.coffee()

salvar_imagem(original, "exemplos/original.png")
salvar_imagem(converter_para_cinza(original), "exemplos/cinza.png")
salvar_imagem(binarizar_imagem(original), "exemplos/binaria.png")
salvar_imagem(redimensionar_imagem(original, 0.5), "exemplos/metade.png")

ajustada = transferir_histograma(original, referencia)
salvar_imagem(ajustada, "exemplos/histograma_transferido.png")
salvar_imagem(encontrar_diferenca(original, ajustada), "exemplos/diferenca.png")

print("Imagens salvas em exemplos/")
