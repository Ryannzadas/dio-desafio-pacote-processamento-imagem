import numpy as np
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte


def ler_imagem(caminho, cinza=False):
    """Lê uma imagem do disco. Com `cinza=True`, já carrega em tons de cinza."""
    return imread(caminho, as_gray=cinza)


def salvar_imagem(imagem, caminho):
    """Salva a imagem no disco. Imagens em float (0 a 1) são convertidas para 0 a 255."""
    imagem = np.asarray(imagem)
    if np.issubdtype(imagem.dtype, np.floating):
        imagem = img_as_ubyte(np.clip(imagem, 0, 1))
    imsave(caminho, imagem, check_contrast=False)
