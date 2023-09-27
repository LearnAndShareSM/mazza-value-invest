
# Finance Data Driven

## Introduction
This repository is dedicated to data-driven financial analysis and models. The codebase primarily utilizes the OpenBB library for data fetching and analysis.

## Prerequisites

- Anaconda or Miniconda installed
- Python 3.9 or above

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