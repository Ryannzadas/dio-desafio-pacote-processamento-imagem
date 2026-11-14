import matplotlib.pyplot as plt


def plot_imagem(imagem):
    """Mostra uma imagem sem eixos."""
    plt.figure(figsize=(12, 4))
    plt.imshow(imagem, cmap="gray")
    plt.axis("off")
    plt.show()


def plot_resultado(*imagens):
    """Mostra as imagens lado a lado; a última recebe o título "Resultado"."""
    quantidade = len(imagens)
    fig, eixos = plt.subplots(nrows=1, ncols=quantidade, figsize=(12, 4), squeeze=False)
    nomes = [f"Imagem {i}" for i in range(1, quantidade)] + ["Resultado"]
    for eixo, nome, imagem in zip(eixos[0], nomes, imagens):
        eixo.set_title(nome)
        eixo.imshow(imagem, cmap="gray")
        eixo.axis("off")
    fig.tight_layout()
    plt.show()


def plot_histograma(imagem):
    """Mostra o histograma de cada canal (vermelho, verde e azul)."""
    fig, eixos = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    cores = ["red", "green", "blue"]
    titulos = ["Vermelho", "Verde", "Azul"]
    for indice, (eixo, cor, titulo) in enumerate(zip(eixos, cores, titulos)):
        eixo.set_title(f"Histograma: {titulo}")
        eixo.hist(imagem[:, :, indice].ravel(), bins=256, color=cor, alpha=0.8)
    fig.tight_layout()
    plt.show()
