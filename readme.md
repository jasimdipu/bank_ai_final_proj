# AI Loan Eligibility Prediction Application

This project is a Django-based web application designed to predict whether a user meets the loan requirements. The application uses AI and machine learning models to perform predictions, and it integrates Celery for asynchronous task management, Redis as a message broker, PostgreSQL for database storage, and Nginx for reverse proxy. Additional services include Flower for Celery monitoring and pgAdmin for managing the PostgreSQL database.

---

## Features

- **Loan Eligibility Prediction**: Users can input their financial and personal details to check if they qualify for a loan.
- **AI Model**: A pre-trained machine learning model is used for predictions.
- **Asynchronous Tasks**: Celery handles time-intensive tasks such as model predictions and data preprocessing.
- **Scalable Architecture**: Dockerized setup with separate services for Django, Celery, Redis, PostgreSQL, and Nginx.
- **Monitoring**: Flower provides real-time insights into Celery tasks.

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Docker**: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- **Docker Compose**: Included with Docker Desktop
- **Git**: [https://git-scm.com/](https://git-scm.com/)

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/jasimdipu/bank_ai_final_proj.git

```

---

### 2. Run the docker command

```bash
docker-compose build
docker-compose up -d
```

### 3. Check that django, pgadmin and other things are running on the url

```djangourlpath
django: localhost:8000
pgadmin: localhost:5050
```
