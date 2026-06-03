# 📊 Portfólio de Ciência de Dados

Bem-vindo ao meu portfólio de projetos. Aqui compartilho projetos que desenvolvi para resolver problemas complexos do mundo real, cobrindo todo o ciclo de vida dos dados: desde a **extração e engenharia de dados em tempo real** até a **modelagem preditiva utilizando Deep Learning**.

Meu objetivo é transformar fluxos de dados brutos e não estruturados em insights estratégicos automatizados.

---


## 📂 Projetos em Destaque

### 1. 📈 Predição de Preços de Ações da Bolsa com Redes Neurais LSTM
**Área:** *Deep Learning, Time Series Forecasting, Finanças Quantitativas*

Este projeto desenvolve um modelo preditivo de alta precisão para séries temporais financeiras, focando na volatilidade e na tendência de fechamento de ativos do mercado de ações.

*   **O Problema:** Preços de ações possuem dependências temporais complexas e ruídos de curtíssimo prazo, tornando modelos de regressão tradicionais ineficientes.
*   **A Solução:** Implementação de uma **Rede Neural Recorrente (RNN)** do tipo **LSTM (Long Short-Term Memory)**, capaz de reter padrões de longo prazo em séries temporais sem sofrer com o problema do desvanecimento do gradiente.
*   **Abordagem Técnica:**
    *   **Pré-processamento:** Limpeza de dados históricos e normalização de escala utilizando o `MinMaxScaler` do *Scikit-Learn*.
    *   **Modelagem:** Arquitetura construída com *TensorFlow/Keras*, empilhando camadas LSTM com mecanismos de regularização (`Dropout`) para mitigar o *overfitting*.
    *   **Validação:** Avaliação baseada em métricas rigorosas de erro, como RMSE (Root Mean Squared Error) e MAE (Mean Absolute Error).
*   **Principais Tecnologias:** `TensorFlow`, `Keras`, `Scikit-Learn`, `Pandas`, `Matplotlib`.
*   **Onde Encontrar:** Pasta /Predicao_acoes_petroleo_b3

---

### 📊 2. Monitor de Inteligência Geopolítica & Econômica (Truth Social)
**Área:** *Data Engineering, Real-Time Streaming, Web Scraping Avançado*

Um pipeline automatizado de extração e monitoramento de dados em tempo real direcionado ao perfil oficial de figuras públicas na plataforma **Truth Social**. O sistema monitora menções a termos estratégicos relacionados a mercado, petróleo e tensões geopolíticas.

*   **O Problema:** Plataformas modernas utilizam ecossistemas SPA (React/Next.js) e firewalls rígidos (Cloudflare), bloqueando raspadores tradicionais (como BeautifulSoup) ou gerando *deadlocks* de carregamento.
*   **A Solução:** Um robô assíncrono programado em modo furtivo (*Stealth*) que, em vez de ler o layout visual (HTML), realiza a **interceptação dos pacotes brutos de API (JSON)** trafegados na rede do navegador.
*   **Abordagem Técnica:**
    *   **Modo Furtivo:** Injeção de scripts para camuflar variáveis de automação (`navigator.webdriver`) e emulação de comportamento humano.
    *   **Otimização:** Bloqueio dinâmico do carregamento de mídias (imagens/fontes) para acelerar a sincronização em 82% e economizar processamento.
    *   **Robustez de String:** Tratamento estrutural de URLs via tabela ASCII para blindar o script contra falhas de codificação de texto (*encoding*) locais do compilador.
*   **Principais Tecnologias:** `Playwright (Async API)`, `Asyncio`, `Regular Expressions (re)`, `Urllib`.
*   **Onde Encontrar:** Pasta /Web_Scapping_TruthSocial

---

## 🛠️ Stack Tecnológica Principal

*   **Linguagens de Programação:** Python (Pandas, NumPy, Scipy)
*   **Inteligência Artificial & Deep Learning:** TensorFlow, Keras, Scikit-Learn
*   **Engenharia de Dados & Automação:** Playwright, Asyncio, Requests, APIs RESTful
*   **Ambientes & Ferramentas:** PyCharm, Git, Virtual Environments (.venv)

---


## 📈 Resultados obtidos no Portfólio

1.  **Domínio em Séries Temporais:** Capacidade de preparar matrizes tridimensionais exigidas por modelos de Deep Learning (`[samples, time steps, features]`) e ajustar hiperparâmetros de redes neurais para previsões financeiras.
2.  **Engenharia de Dados Resiliente:** Desenvolvimento de scripts preparados para lidar com falhas de rede, oscilações de servidores e bloqueios automatizados de plataformas web.
3.  **Código Limpo e Assíncrono:** Uso avançado de programação orientada a eventos e programação assíncrona (`async/await`) em Python para otimização de performance.

---
