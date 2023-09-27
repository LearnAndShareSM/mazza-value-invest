
# Finance Data Driven

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
