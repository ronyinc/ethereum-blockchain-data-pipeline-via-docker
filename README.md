# Ethereum Blockchain Data Pipeline

> End-to-end modern Data Engineering platform built with Apache Airflow, Docker, dbt Core, Snowflake, AWS S3 and GitHub Actions.

---

## Overview

This project demonstrates how to build a modern ELT data engineering platform that ingests publicly available Ethereum blockchain datasets from Amazon S3 into Snowflake using Apache Airflow, and transforms the raw data into analytics-ready models using dbt Core.

The goal of the project is to simulate a real-world cloud ELT pipeline by combining modern data engineering tools into a cohesive architecture.


The platform includes:

- Containerized infrastructure using Docker
- Workflow orchestration with Apache Airflow
- Secure Snowflake integration using RSA key-pair authentication
- Raw data storage in AWS S3
- Data warehousing in Snowflake
- Data transformation using dbt Core
- CI/CD using GitHub Actions
- Analytics-ready dimensional models

---

# Architecture

![Architecture Diagram](docs/architecture-diagram.png)

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Orchestration | Apache Airflow |
| Containerization | Docker & Docker Compose |
| Data Warehouse | Snowflake |
| Data Transformation | dbt Core |
| Cloud Storage | AWS S3 |
| Metadata Database | PostgreSQL |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions |
| Operating System | Ubuntu Linux |

---

# Project Architecture

The pipeline follows a modern ELT architecture.

```
Ethereum Blockchain Dataset
(AWS Public Blockchain Dataset)
             │
             ▼
AWS S3
s3://aws-public-blockchain/v1.0/eth/
             │
             ▼
Snowflake External Stage
             │
             ▼
Airflow DAG
(COPY INTO)
             │
             ▼
Snowflake RAW Database
             │
             ▼
dbt Core
             │
             ▼
Analytics Models
             │
             ▼
Business Intelligence & Reporting

---

# Repository Structure

```
ethereum-blockchain-data-pipeline/
│
├── dags/
├── dbt/
├── dbt_profiles/
├── docs/
│   └── architecture-diagram.png
├── plugins/
├── docker-compose.yml
├── Dockerfile.airflow
├── requirements.txt
└── README.md
```

---

# Features

- Dockerized development environment
- Airflow DAG orchestration
- Secure Snowflake RSA authentication
- AWS S3 raw data landing layer
- dbt modular transformations
- CI/CD using GitHub Actions
- Analytics-ready dimensional models
- Scalable architecture for future blockchain datasets

---

# Current Pipeline

The current implementation performs the following:

1. Ethereum blockchain datasets are published daily to the AWS Public Blockchain S3 bucket.
2. Snowflake External Stages provide access to the source files stored in Amazon S3.
3. Apache Airflow orchestrates SQL-based COPY INTO operations that load the latest blockchain data into Snowflake RAW tables.
4. Data is loaded into Snowflake RAW tables.
5. dbt transforms raw data into staging models.
6. dbt builds intermediate models.
7. dbt creates analytics-ready mart tables.

---

# Airflow Architecture

The Airflow deployment consists of:

- Airflow Webserver
- Airflow Scheduler
- PostgreSQL Metadata Database
- Docker Compose
- Snowflake Provider
- Python Operators
- Snowflake Hooks

---

# dbt Project Structure

The dbt project follows a layered architecture:

```
RAW
    │
    ▼
Staging
    │
    ▼
Intermediate
    │
    ▼
Marts
```

---

# CI/CD Pipeline

GitHub Actions automatically performs:

- dbt deps
- dbt parse
- dbt build
- dbt tests
- Slim CI
- Deployment validation

---

# Security

Sensitive credentials are **never committed** to GitHub.

The project uses:

- Snowflake RSA key-pair authentication
- Environment variables
- Docker secrets/volumes
- GitHub Secrets for CI/CD


# Learning Objectives

This project was built to gain hands-on experience with:

- Apache Airflow
- Docker
- Snowflake
- dbt Core
- Python
- AWS S3
- GitHub Actions
- Modern ELT architecture
- Production-style Data Engineering workflows

---

## Disclaimer

This project uses the AWS Public Blockchain Dataset as its source of Ethereum blockchain data. It is intended for educational and portfolio purposes and is not affiliated with Amazon Web Services, the Ethereum Foundation, or any blockchain data provider.



# License

This project is licensed under the MIT License.

