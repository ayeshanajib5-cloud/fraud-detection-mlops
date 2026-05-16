# AWS App Runner Deployment Plan

This document explains the planned AWS deployment approach for the fraud detection MLOps API.

## Deployment Target

The FastAPI application will be deployed using AWS App Runner because the project is already Dockerized and has a working API structure. App Runner is suitable for running containerized web APIs without manually managing servers.

## Required AWS Access

To deploy the project, access is needed to an AWS account with permissions for:

- AWS App Runner
- Amazon ECR
- CloudWatch Logs
- IAM role creation or IAM role selection
- GitHub repository connection

## Deployment Steps

1. Open AWS App Runner.
2. Create a new App Runner service.
3. Select GitHub repository as the source.
4. Connect the repository: `fraud-detection-mlops`.
5. Choose Dockerfile-based deployment.
6. Select the `main` branch.
7. Configure the service port as `8000`.
8. Start deployment.
9. Wait until the service status becomes running.
10. Test the live API endpoints.

## Environment Details

The application uses:

- Python
- FastAPI
- Uvicorn
- Docker
- Scikit-learn
- Joblib
- Prometheus client

The API runs on port:

```text
8000