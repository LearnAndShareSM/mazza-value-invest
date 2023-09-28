
# Finance Data Driven

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
