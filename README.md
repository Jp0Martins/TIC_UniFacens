# FlowMind – Inferência de Mobilidade Urbana com IA

O **FlowMind** é um projeto de Inteligência Artificial voltado à inferência de padrões de mobilidade urbana a partir de dados fragmentados de sensores de tráfego. Utilizando técnicas de análise de dados, clusterização espacial e modelagem probabilística, o projeto demonstra como reconstruir padrões de deslocamento mesmo quando os dados não informam explicitamente a origem e o destino das viagens.

> **⚠️ Importante:** Devido ao limite de armazenamento do GitHub, este repositório contém **apenas a Fase 9** do projeto (Validação, Visualização e Entrega), juntamente com a documentação e os materiais necessários para compreender e executar a etapa final.

---

# 📂 Conteúdo do Repositório

```
📁 app/
📁 src/
📁 data/
📄 FlowMind.pdf
📄 Documentação das Fases.pdf
📄 rodar.bat
📄 README.md
```

### Arquivos disponíveis

* **FlowMind.pdf** – Apresentação resumida do projeto.
* **Documentação das Fases.pdf** – Documentação completa das nove fases do MVP.
* **Fase 9** – Dashboard final e códigos responsáveis pela visualização dos resultados.
* **rodar.bat** – Script para executar automaticamente toda a aplicação.

---

# Problema de Negócio

Gestores públicos precisam compreender os padrões de deslocamento urbano para melhorar o planejamento da mobilidade. Entretanto, os sensores de trânsito registram apenas:

* Placa do veículo;
* Local da passagem;
* Data;
* Horário.

Essas informações não revelam diretamente a origem e o destino das viagens. O desafio do projeto é utilizar Inteligência Artificial para inferir esses deslocamentos a partir de dados incompletos.

---

# Objetivo

Desenvolver um pipeline completo capaz de transformar aproximadamente **21 milhões de registros de sensores de tráfego** em informações estratégicas para apoiar decisões de mobilidade urbana.

---

# Estratégia de IA

A solução foi desenvolvida em quatro grandes etapas:

## 1. Pré-processamento

* Limpeza dos dados;
* Padronização;
* Conversão para Parquet;
* Organização temporal.

## 2. Clusterização Espacial

* Agrupamento dos sensores em zonas urbanas utilizando **K-Means**.

## 3. Inferência de Trajetórias

* Construção das sessões de viagem;
* Extração dos pares origem-destino.

## 4. Modelagem Probabilística

* Matrizes Origem-Destino;
* Cadeias de Markov;
* Inferência probabilística dos deslocamentos.

### Por que essa abordagem?

* Funciona com dados incompletos;
* Não depende de dados rotulados (aprendizado não supervisionado);
* Lida naturalmente com incertezas;
* Produz resultados interpretáveis.

---

# Estrutura do MVP

## A. Fundação e Preparação dos Dados (Fases 1 e 2)

**Objetivo**

Transformar dados brutos em uma base confiável para análise.

**Principais atividades**

* Limpeza de aproximadamente 21 milhões de registros;
* Tratamento de inconsistências;
* Conversão para Parquet;
* Organização cronológica das passagens dos veículos.

---

## B. Inteligência Espacial (Fases 3 e 4)

**Objetivo**

Reduzir a complexidade espacial da cidade.

**Principais atividades**

* Clusterização dos 26 sensores;
* Criação das zonas urbanas;
* Definição das sessões de viagem.

---

## C. Modelagem Estatística e Probabilística (Fases 5 e 6)

**Objetivo**

Inferir padrões de deslocamento urbano.

**Principais atividades**

* Matrizes Origem-Destino;
* Cadeias de Markov;
* Probabilidades de transição entre zonas.

---

## D. Validação e Dashboard (Fases 7, 8 e 9)

**Objetivo**

Validar o modelo e apresentar os resultados de forma visual.

**Principais atividades**

* Avaliação das métricas;
* Testes de robustez;
* Dashboard em Streamlit;
* Consolidação dos resultados.

---

# Principais Resultados

Após todo o pipeline, foram processados aproximadamente:

* **21.061.609 registros**
* **1.440.237 placas únicas**
* **26 sensores**
* **113 dias de monitoramento**

Entre os principais resultados obtidos:

* Identificação dos principais corredores urbanos;
* Construção de matrizes probabilísticas Origem-Destino;
* Inferência de trajetórias utilizando Cadeias de Markov;
* Identificação do fluxo **Zona 3 → Zona 1** como o principal corredor inter-zona no período da tarde, com **246.108 deslocamentos**.

---

# Impacto Esperado

O projeto pode auxiliar órgãos públicos em diversas aplicações:

* 🚦 Identificação dos corredores de maior tráfego;
* 🚌 Planejamento e otimização do transporte público;
* 🏙️ Apoio ao planejamento urbano;
* 🌐 Simulação de cenários utilizando Gêmeos Digitais (Digital Twins).

---

# Tecnologias Utilizadas

* Python
* Pandas
* DuckDB
* NumPy
* Scikit-learn
* K-Means
* Cadeias de Markov
* Plotly
* Streamlit
* Apache Parquet
* Git
* GitHub

---

# Como Executar

## Opção 1 (Recomendado)

Basta dar **dois cliques** no arquivo:

```text
rodar.bat
```

O script irá automaticamente:

1. Verificar se o Python está instalado;
2. Instalar as dependências necessárias;
3. Preparar a base do dashboard;
4. Iniciar a aplicação no Streamlit.

---

## Opção 2 (Manual)

### Instalar as dependências

```bash
pip install streamlit pandas duckdb plotly pyarrow
```

### Preparar a base do dashboard

```bash
python src/preparar_base_dashboard.py
```

### Executar a aplicação

```bash
streamlit run app/dashboard.py
```

Após iniciar, o navegador abrirá automaticamente no endereço:

```
http://localhost:8501
```

---

# Observações

Este repositório contém apenas a **Fase 9** do projeto devido às limitações de armazenamento do GitHub. As fases anteriores são documentadas no arquivo **Documentação das Fases.pdf**, permitindo compreender toda a metodologia utilizada para construção do pipeline analítico.

---

# Autor

**João Pedro Pereira Martins**

Projeto desenvolvido entre **abril e maio de 2026**, com foco na aplicação de Inteligência Artificial, Ciência de Dados e Modelagem Probabilística para apoio ao planejamento da mobilidade urbana.
