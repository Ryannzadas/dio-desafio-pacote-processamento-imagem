"""Testes rápidos com as imagens de exemplo que vêm no scikit-image.

Rode com:  python -m unittest discover tests
"""

import os
import tempfile
import unittest

import numpy as np
from skimage import data

from processamento_imagem.processamento import (
    binarizar_imagem,
    converter_para_cinza,
    encontrar_diferenca,
    redimensionar_imagem,
    transferir_histograma,
)
from processamento_imagem.utilidades import ler_imagem, salvar_imagem


class TestProcessamento(unittest.TestCase):
    def setUp(self):
        self.astronauta = data.astronaut()  # 512x512x3, uint8
        self.cafe = data.coffee()[:400, :600]

    def test_diferenca_entre_imagens_iguais(self):
        diferenca = encontrar_diferenca(self.astronauta, self.astronauta)
        self.assertEqual(diferenca.shape, self.astronauta.shape[:2])
        self.assertEqual(diferenca.max(), 0)

    def test_diferenca_normalizada(self):
        ruido = np.clip(self.astronauta.astype(int) + 40, 0, 255).astype(np.uint8)
        diferenca = encontrar_diferenca(self.astronauta, ruido)
        self.assertAlmostEqual(float(diferenca.min()), 0.0)
        self.assertAlmostEqual(float(diferenca.max()), 1.0)

    def test_transferir_histograma(self):
        resultado = transferir_histograma(self.astronauta, self.cafe)
        self.assertEqual(resultado.shape, self.astronauta.shape)

    def test_redimensionar(self):
        menor = redimensionar_imagem(self.astronauta, 0.25)
        self.assertEqual(menor.shape, (128, 128, 3))
        with self.assertRaises(AssertionError):
            redimensionar_imagem(self.astronauta, 1.5)

    def test_cinza(self):
        cinza = converter_para_cinza(self.astronauta)
        self.assertEqual(cinza.shape, (512, 512))
        self.assertEqual(cinza.dtype, np.uint8)
        # mesmo cálculo do artigo, para um pixel
        r, g, b = self.astronauta[100, 100].astype(float)
        self.assertEqual(cinza[100, 100], int(0.299 * r + 0.587 * g + 0.114 * b))

    def test_binarizar(self):
        binaria = binarizar_imagem(converter_para_cinza(self.astronauta))
        self.assertEqual(set(np.unique(binaria)), {0, 255})
        self.assertEqual(binarizar_imagem(np.array([[127, 128]], dtype=np.uint8)).tolist(), [[0, 255]])


class TestUtilidades(unittest.TestCase):
    def test_salvar_e_ler(self):
        imagem = data.astronaut()
        with tempfile.TemporaryDirectory() as pasta:
            caminho = os.path.join(pasta, "astronauta.png")
            salvar_imagem(imagem, caminho)
            self.assertTrue(np.array_equal(ler_imagem(caminho), imagem))
            self.assertEqual(ler_imagem(caminho, cinza=True).ndim, 2)
            salvar_imagem(redimensionar_imagem(imagem, 0.5), caminho)  # float 0..1


if __name__ == "__main__":
    unittest.main()
