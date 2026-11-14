import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def encontrar_diferenca(imagem1, imagem2):
    """Compara duas imagens coloridas do mesmo tamanho.

    Imprime a similaridade estrutural (SSIM, de -1 a 1) e devolve o mapa de
    diferenças normalizado entre 0 e 1.
    """
    assert imagem1.shape == imagem2.shape, "Informe 2 imagens com o mesmo formato!"
    cinza1 = rgb2gray(imagem1)
    cinza2 = rgb2gray(imagem2)
    score, diferenca = structural_similarity(cinza1, cinza2, full=True, data_range=1.0)
    print("Similaridade das imagens:", score)
    minimo, maximo = np.min(diferenca), np.max(diferenca)
    if maximo == minimo:
        return np.zeros_like(diferenca)
    return (diferenca - minimo) / (maximo - minimo)


def transferir_histograma(imagem, referencia):
    """Ajusta as cores de `imagem` para seguir o histograma de `referencia`."""
    return match_histograms(imagem, referencia, channel_axis=-1)
