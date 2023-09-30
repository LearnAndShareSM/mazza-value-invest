
# Finance Data Driven

Costruzione di una piattaforma che consente di elaborare dati provenienti da diverse fonti e trasformarli in insight tramite modelli di machine learning e analisi statistiche

## FASE 1
- Nella fase uno i dati proverranno da varie API (stock prices, financial statements, etc.) che forniscono dati finanziari con una determinata frequenza (il pulling dei dati sarà al momento 1 volta al giorno, ma in futuro prevedo di diminuire di molto la frequenza per arrivare quasi al "real time" utilizzzando per esempio Apache Kafka along with Kafka Connectors for various APIs.)
- voglio utilizzare sempre ubuntu come sistema operativo
- utilizzo git e github per il versionamento del codice 
- questi flussi dati devono essere puliti e processati (handling missing data, outliers, check data quality, ecc.) per essere utilizzati insieme per creare delle features utili sia ai vari modelli di addestramento, sia alle analisi che si vuole poi esporre. Serve quindi costruire un'intera pipeline che faccia tutto ciò (al momento voglio utlizzare principalmente python ed SQL o pyspark se oppurtuno, con librerie con pandas, polars e dask, ma suggeriscimi linguaggi e strumenti aggiuntivi che ritieni opportuno)
- nella prima fase utilizzerò modelli supervisionati (per esempio xgboost, ma in futuro vorrò testare anche modelli di deep learning). Sicuramente userò scikit-learn, mlflow e optuna per la parte di MLOps, ma suggeriscimi altre librerie o framework emergenti per gestire la parte di mlops. 
- per la storicizzazione dei dati vorrei alternare la costruzione di una datalake house (considera per esempio Apache Iceberg e Delta Lake come strumenti), dabase relazionali (PostgreSQL) o non relazionali (mongoDB) a seconda delle eseginze e dalla mole/tipo di dato da storicizzare
- utilizza Feast as feature store
- per la parte di Monitoring and Evaluation oltre ad MLFlow e Prometheus e soluzioni custom
- Testing and Validation: Implement rigorous testing and validation procedures to ensure data integrity and model accuracy.
- Architecture: Establish a microservices architecture can be beneficial for scalability and maintainability. Each component (data ingestion, processing, ML model serving, front-end) can be developed, deployed, and scaled independently.
- Documentation: Maintain thorough documentation for code, architecture, and user manuals for long-term maintainability and developer onboarding.
- voglio impostare una piattaforma scalabile in tutti gli aspetti sia in termini di prestazioni, sia in termini di costo. Inizialmente per il POC voglio spendere il meno possibile, ma non appena ho qualche cliente pagante avrò la necessità di scalare in modo proporzionale al numero di clienti che sottoscriveranno l'abbonamento alla mia piattaforma
- Per la parte di backend usa FastAPI
- Per la parte di microservices e orchiestrazione considera di utilizzare Docker e Kubernetis
- avrò quindi bisogno di un deployment environment hybrid, dove posso testare tutto on-premises in locale sul mio pc, ma avere la possibile di deployare inizialmente un POC per vendere la soluzione. Non appena venduta al primo cliente devo avere la possibilità di deployare il prodotto completo in un ottica scalabile con il numero di clienti. Suggerisci tu le migliori opzioni nelle varie parti di architettura necessarie per implementare la mia strategia (ricorda inizialmente posso spendere poco, almeno fino a quando non avrò il mio primo cliente)
- i risultati vanno ad alimentare tabelle e grafici interrogabili tramite frontend. Sicuramente utilizzerò React, Next.js e D3.js  e GraphQL for more flexible queries to your backend.
- non ho una scadenza specifica per questo progetto. Sarà un progetto a lungo termine di cui questa è solo la fase 1





























Progetto con il quale in seguito all'elaborazione dati questi vengono salvati in un db, e i dati dal db vengono letti dal frontend react per essere interrogati

Requisiti funzionali:

Voglio creare una web app che che parla di finanza, sia attraverso contenuti scritti sia attraverso l’analisi dinamica dei dati finanziari con tabelle e grafici, con i seguenti requisiti funzionali di base:

- home page che introduce al sito web e spiega cosa fa
- una pagina di alert in cui è contenuta una tabella con dei dati relativi a vari asset. La tabella è letta da un db che al momento si tratta essere di un db sqlachemy
- altra sezione formato blog con un elenco di articoli


## Introduction
This repository is dedicated to data-driven financial analysis and models. The codebase primarily utilizes the OpenBB library for data fetching and analysis.

Nella parte di notebook lavoreremo con openBB in modo da richiamare i dati e storicizzarli o in una data lake house o un un DB



## Installation


### Install OpenBB

For a complete guide on installing OpenBB, refer to the official documentation [here](https://docs.openbb.co/terminal/installation/pypi).

In this specific case, the following commands were executed to set up the environment and install OpenBB:

1. Create a new conda environment:
```bash
conda env create -n obb --file https://raw.githubusercontent.com/OpenBB-finance/OpenBBTerminal/main/build/conda/conda-3-9-env.yaml
```

2. Activate the conda environment:
```bash
conda activate obb
```

3. Install OpenBB:
```bash
pip install openbb --no-cache-dir
```



Aggiungi il file .env al backend con le credenziali

FMP_SECRET_KEY=<your_key>
DATABASE_PATH=<your_database>


Per lavorare con il backend

cd backend
conda env create -f environment.yml
