from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [linha.strip() for linha in f if linha.strip() and not linha.startswith("#")]

setup(
    name="processamento-imagem-ryannzadas",
    version="0.1.0",
    author="João Ryan",
    description="Pacote de processamento de imagens com scikit-image (desafio DIO)",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ryannzadas/dio-desafio-pacote-processamento-imagem",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    python_requires=">=3.9",
)
