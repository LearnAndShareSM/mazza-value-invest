
# Finance Data Driven Platform

## Table of Contents

1. [Overview](#overview)
2. [Project Phases](#project-phases)
3. [Technology Stack](#technology-stack)
4. [Features](#features)
    - [Data Ingestion](#data-ingestion)
    - [Data Processing](#data-processing)
    - [Machine Learning](#machine-learning)
    - [Data Storage](#data-storage)
    - [Monitoring and Evaluation](#monitoring-and-evaluation)
5. [Architecture](#architecture)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Microservices and Orchestration](#microservices-and-orchestration)
6. [Deployment](#deployment)
7. [Development Diary](#development-diary)
8. [Contributing](#contributing)
9. [License](#license)
10. [Subscribe](#subscribe)

## Overview

The Finance Data Driven Platform is designed to offer data-driven insights to aid investment decision-making by processing data from various sources and applying machine learning models and statistical analysis. This repository hosts the code and resources for the current and future development stages. This platform is part of a series of articles that serve as a journal detailing the project's progress.

## Project Phases

The project is divided into multiple phases. The first phase focuses on data sourcing, data storage, data processing, modeling, monitoring and evaluation, frontend development, architecture, and deployment environment.

## Technology Stack

- **Operating System**: Ubuntu
- **Version Control**: Git and GitHub
- **Languages**: Python, SQL, PySpark
- **Libraries**: Pandas, Polars, Dask, scikit-learn, MLFlow, Optuna
- **Web Framework**: FastAPI for Backend, React and Next.js for Frontend
- **Data Visualization**: D3.js
- **Query Language**: GraphQL
- **Containerization**: Docker
- **Orchestration**: Kubernetes

## Features

### Data Ingestion

- Data is sourced from APIs like OpenBB and FinancialModelingPrep.
- Initial data frequency is once a day, with plans to increase to near real-time.
- Future considerations include utilizing Apache Kafka and Kafka Connectors.

### Data Processing

- Comprehensive data pipelines for cleaning and processing.
- Handle missing data, outliers, and ensure data quality.
- Conduct feature engineering using Python and PySpark, with libraries like Pandas, Polars, and Dask.

### Machine Learning

- Utilizes both classic financial asset evaluation models and supervised models like XGBoost.
- In-depth study of target variables.
- MLOps tools include MLFlow and Optuna.

### Data Storage

- Data lake houses like Apache Iceberg and Delta Lake.
- Relational databases like PostgreSQL and NoSQL databases like MongoDB.
- Feature storage through Feast.

### Monitoring and Evaluation

- MLFlow for model tracking, Prometheus for system monitoring.
- Custom monitoring solutions are also being considered.

## Architecture

### Backend

- Developed using FastAPI for high performance and scalability.

### Frontend

- Utilizes React, Next.js, and D3.js for data visualization.
- GraphQL for flexible queries to the backend.

### Microservices and Orchestration

- Microservices architecture for scalability and maintainability.
- Docker and Kubernetes for containerization and orchestration.

## Deployment

- Hybrid deployment environment for local on-premises testing and initial POC deployments.
- Architecture will scale in line with customer growth.


## Development Diary

This section serves as a diary where we document the various episodes in the development of this project. Each episode is published on Substack and focuses on specific aspects and progress.

### Episodes

1. **Introduction to the Finance Data Driven Platform**  
   - [Episode 1 - Kickstart](https://saveriomazza.substack.com/p/building-a-data-analytics-platform)


## Contributing

Please read the documentation for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


---

This README is a living document and will be updated as the project evolves. Suggestions for additional tools and technologies are welcome.
