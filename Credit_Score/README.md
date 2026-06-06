# Previsão de Score de Crédito 💳

Este projeto desenvolve um modelo preditivo baseado em machine learning para calcular o score de crédito de clientes com base em seu perfil socioeconômico e patrimonial. O objetivo principal é automatizar a análise de risco financeiro para apoiar a tomada de decisões de concessão de crédito. Este repositório integra meu portfólio de Ciência de Dados.

## 🛠️ Tecnologias e Ferramentas

*   **Linguagem:** Python
*   **Manipulação de Dados:** Pandas, NumPy
*   **Visualização de Dados:** Seaborn, Matplotlib
*   **Machine Learning:** Scikit-Learn

## 📊 Estrutura dos Dados

O conjunto de dados possui **10.474 registros** sem valores nulos, contendo as seguintes variáveis:

*   `UF`: Estado de residência do cliente.
*   `IDADE` / `FAIXA_ETARIA`: Idade e agrupamento etário do cliente.
*   `ESCOLARIDADE` / `ESTADO_CIVIL`: Informações sociodemográficas.
*   `QT_FILHOS`: Quantidade de dependentes.
*   `CASA_PROPRIA` / `QT_IMOVEIS` / `VL_IMOVEIS`: Dados de patrimônio imobiliário.
*   `OUTRA_RENDA` / `OUTRA_RENDA_VALOR`: Existência e valor de fontes secundárias de renda.
*   `TEMPO_ULTIMO_EMPREGO_MESES` / `TRABALHANDO_ATUALMENTE`: Histórico de estabilidade profissional.
*   `ULTIMO_SALARIO`: Renda principal do cliente.
*   `QT_CARROS` / `VALOR_TABELA_CARROS`: Dados de patrimônio automotivo.
*   `SCORE` (**Variável Alvo**): Pontuação numérica do risco de crédito.

## 📈 Metodologia e Performance

O projeto seguiu o fluxo padrão de desenvolvimento em Ciência de Dados:

1.  **Análise Exploratória (EDA):** Análise de distribuição do score e tratamento de outliers.
2.  **Pré-processamento:** Validação dos tipos de dados e estruturação das variáveis numéricas e categóricas já codificadas em formato inteiro e ponto flutuante.
3.  **Modelagem:** Aplicação do algoritmo de **Regressão Linear** para a predição da pontuação contínua do score.

### Resultado do Modelo

O modelo apresentou uma sólida capacidade preditiva para o cenário de negócios:

*   **Coeficiente de Determinação (R² Score):** **79,5%**

Este resultado indica que 79,5% da variabilidade do score de crédito é explicada pelas características demográficas, profissionais e patrimoniais integradas no modelo.
