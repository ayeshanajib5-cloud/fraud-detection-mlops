# Production Readiness Checklist

## Completed

- FastAPI inference API
- Docker containerization
- MLflow experiment tracking
- GitHub Actions CI/CD
- Pytest API testing
- Input validation
- Prometheus `/metrics` endpoint
- Health check `/health` endpoint
- Architecture diagram
- AWS App Runner deployment plan

## Before Deployment

- Confirm Docker build works locally
- Confirm `/health` works locally
- Confirm `/docs` opens locally
- Confirm `/metrics` works locally
- Confirm `/predict` works with valid input
- Confirm invalid input returns a clear error
- Confirm GitHub Actions is green

## After Deployment

- Test live `/docs`
- Test live `/health`
- Test live `/metrics`
- Test live `/predict`
- Check CloudWatch logs
- Add live API URL to README