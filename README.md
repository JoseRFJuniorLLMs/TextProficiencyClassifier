# Classificação de Textos por Níveis de Proficiência em Inglês


Este projeto classifica textos em um arquivo JSON com base nos níveis de proficiência em inglês, adicionando um campo "level" a cada item. A classificação é feita usando índices de legibilidade, análise de complexidade gramatical e análise de vocabulário.



## Índices de Legibilidade

### Flesch-Kincaid Grade Level

O índice Flesch-Kincaid Grade Level mede o nível de escolaridade necessário para entender o texto. É calculado com base no número de palavras, sentenças e sílabas no texto.

### Gunning Fog Index

O índice Gunning Fog mede a complexidade do texto com base no número de palavras complexas (palavras com três ou mais sílabas) e no comprimento das frases. Ele estima o número de anos de educação formal necessários para entender o texto em uma leitura única.

### SMOG Index

O índice SMOG (Simple Measure of Gobbledygook) mede a legibilidade do texto contando o número de palavras polissilábicas em amostras de 30 frases. É frequentemente usado em textos médicos e de saúde para garantir que sejam compreensíveis para o público em geral.

## Complexidade Gramatical

A análise de complexidade gramatical envolve a análise da estrutura das frases, incluindo a utilização de frases subordinadas e coordenadas.

### Frases Subordinadas

Frases subordinadas são aquelas que dependem de outra frase para completar seu sentido. Elas são introduzidas por conjunções subordinativas, como "porque", "embora", "quando", etc.

### Frases Coordenadas

Frases coordenadas são aquelas que são independentes e são ligadas por conjunções coordenativas, como "e", "mas", "ou", etc.

## Vocabulário Avançado


A análise de vocabulário avançado envolve identificar palavras que estão fora das listas de alta frequência. Isso inclui:

### Palavras de Alta Frequência

Palavras que são comumente usadas no cotidiano e geralmente são entendidas por falantes nativos de nível básico.

### Palavras Avançadas

Palavras que não estão nas listas de alta frequência e indicam um vocabulário mais sofisticado.

## Como Usar

### Prepare o ambiente

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as dependências executando:
   ```sh
   pip install -r requirements.txt
#   T e x t P r o f i c i e n c y C l a s s i f i e r 
 
 
