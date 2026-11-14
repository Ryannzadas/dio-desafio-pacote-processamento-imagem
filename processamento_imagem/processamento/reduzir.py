"""Redução de dimensionalidade: de 3 canais (RGB) para 1 (cinza) e de 256
níveis para 2 (preto e branco).

Adaptado do artigo "Redução de dimensionalidade em imagens usando Python"
(DIO). O artigo percorre os pixels um a um com Pillow; aqui as mesmas
fórmulas são aplicadas de uma vez com NumPy, o que é bem mais rápido.
"""

import numpy as np

PESOS_RGB = np.array([0.299, 0.587, 0.114])


def _para_uint8(imagem):
    """Leva a imagem para inteiros de 0 a 255 (o scikit-image às vezes devolve floats de 0 a 1)."""
    imagem = np.asarray(imagem)
    if np.issubdtype(imagem.dtype, np.floating):
        return np.clip(imagem * 255, 0, 255).astype(np.uint8)
    return imagem.astype(np.uint8)


def converter_para_cinza(imagem):
    """Converte uma imagem RGB em tons de cinza (0 a 255).

    Usa a média ponderada 0,299·R + 0,587·G + 0,114·B. Um canal alfa, se houver, é ignorado.
    """
    imagem = _para_uint8(imagem)
    if imagem.ndim == 2:
        return imagem
    cinza = imagem[..., :3].astype(np.float64) @ PESOS_RGB
    return cinza.astype(np.uint8)


def binarizar_imagem(imagem_cinza, limiar=127):
    """Deixa a imagem só em preto (0) e branco (255).

    Pixels acima do limiar viram brancos; os demais viram pretos.
    """
    cinza = converter_para_cinza(imagem_cinza)
    return np.where(cinza > limiar, 255, 0).astype(np.uint8)
