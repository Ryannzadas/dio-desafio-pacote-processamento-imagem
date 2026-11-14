# processamento-imagem-ryannzadas

Pacote Python de processamento de imagens feito no desafio de projeto da
[DIO](https://www.dio.me/). O foco do desafio é a estrutura de
empacotamento: `setup.py`, `requirements.txt`, build e publicação no PyPI.

Este repositório é um fork do
[projeto de referência](https://github.com/charlesfsouza/dio-desafio-pacote-processamento-imagem).
Corrigi os erros que impediam o pacote de funcionar com as bibliotecas atuais
e acrescentei a redução de dimensionalidade do artigo
[Redução de Dimensionalidade em Imagens usando Python](https://www.dio.me/articles/reducao-de-dimensionalidade-em-imagens-usando-python).

![Original, cinza, binária, histograma transferido e mapa de diferenças](exemplos/prancha.png)

## O que o pacote faz

**`processamento_imagem.processamento`**

| Função | O que faz |
|--------|-----------|
| `encontrar_diferenca(imagem1, imagem2)` | Mostra a similaridade estrutural (SSIM) e devolve o mapa de diferenças. |
| `transferir_histograma(imagem, referencia)` | Ajusta as cores de uma imagem pelo histograma de outra. |
| `redimensionar_imagem(imagem, proporcao)` | Reduz a imagem pela proporção (0 a 1). |
| `converter_para_cinza(imagem)` | RGB para tons de cinza: 0,299·R + 0,587·G + 0,114·B. |
| `binarizar_imagem(imagem, limiar=127)` | Só preto e branco: acima do limiar vira branco. |

**`processamento_imagem.utilidades`**

| Função | O que faz |
|--------|-----------|
| `ler_imagem(caminho, cinza=False)` | Lê a imagem do disco. |
| `salvar_imagem(imagem, caminho)` | Salva a imagem (converte float 0–1 para 0–255). |
| `plot_imagem(imagem)` | Mostra uma imagem. |
| `plot_resultado(*imagens)` | Mostra várias imagens lado a lado. |
| `plot_histograma(imagem)` | Mostra o histograma de cada canal RGB. |

## Uso

```python
from processamento_imagem.processamento import binarizar_imagem, converter_para_cinza
from processamento_imagem.utilidades import ler_imagem, plot_resultado

imagem = ler_imagem("foto.jpg")
cinza = converter_para_cinza(imagem)
binaria = binarizar_imagem(cinza)
plot_resultado(imagem, cinza, binaria)
```

O arquivo [`exemplo.py`](exemplo.py) usa uma imagem que já vem no
scikit-image e gera os resultados da figura acima na pasta `exemplos/`.

## Correções em relação à referência

O código original não rodava. Estes foram os problemas e como os resolvi:

| Problema | Correção |
|----------|----------|
| A pasta do pacote se chamava `dio-desafio-pacote-processamento-imagem`. Com hífens, o Python não consegue importá-la. | Renomeada para `processamento_imagem`. |
| `image1.shappe` (erro de digitação) quebrava `encontrar_diferenca`. | `imagem1.shape`. |
| `dif_image.np.min(dif_image)` não existe; a normalização estava errada. | `(dif - min) / (max - min)`, tratando o caso de imagens idênticas. |
| `redimensionar_imagem` usava a variável `imagem`, que não existia. | Nome da variável corrigido. |
| `match_histograms(..., multichannel=True)`: o parâmetro foi removido no scikit-image 0.19. | `channel_axis=-1`. |
| `structural_similarity` em imagens float exige `data_range` nas versões novas. | `data_range=1.0`. |
| `plot_result` com uma única imagem quebrava (`subplots` não devolve lista). | `squeeze=False`. |
| O `requirements.txt` não ia para o pacote, então `python -m build` falhava ao gerar o wheel. | Adicionado o `MANIFEST.in`. |
| O nome `dio-desafio-pacote-processamento-imagem` já está ocupado no PyPI. | Novo nome: `processamento-imagem-ryannzadas`. |

Sobre o artigo da Opção B: ele percorre os pixels um a um com Pillow. Aqui as
mesmas fórmulas (pesos 0,299/0,587/0,114 e limiar 127) são aplicadas de uma vez
com NumPy, o que é muito mais rápido em imagens grandes.

Versões testadas: Python 3.13, NumPy 2.5, scikit-image 0.26 e Matplotlib 3.11.

## Testes

```bash
pip install -r requirements.txt
python -m unittest discover tests
```

## Como gerar e publicar o pacote

```bash
python -m pip install --upgrade build twine
python -m build                      # gera dist/*.tar.gz e dist/*.whl
python -m twine check dist/*         # valida o pacote
python -m twine upload --repository testpypi dist/*   # Test PyPI
python -m twine upload dist/*                         # PyPI
```

No upload, o usuário é `__token__` e a senha é o token de API criado na sua
conta do [Test PyPI](https://test.pypi.org/manage/account/) ou do
[PyPI](https://pypi.org/manage/account/).

Depois de publicado:

```bash
pip install processamento-imagem-ryannzadas
```

## Autor

João Ryan, a partir do projeto de Charles ([charlesfsouza](https://github.com/charlesfsouza)).
