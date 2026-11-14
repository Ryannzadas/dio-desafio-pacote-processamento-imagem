from skimage.transform import resize


def redimensionar_imagem(imagem, proporcao):
    """Redimensiona a imagem pela proporção informada (0 < proporcao <= 1)."""
    assert 0 < proporcao <= 1, "Informe uma proporção maior que 0 e até 1!"
    altura = round(imagem.shape[0] * proporcao)
    largura = round(imagem.shape[1] * proporcao)
    return resize(imagem, (altura, largura), anti_aliasing=True)
