# Project 8 – Deployment Completion

## Week 5

The API was completed with:
- Input validation using Pydantic
- Health-check endpoint
- Prediction endpoint
- Swagger/OpenAPI documentation
- Docker configuration
- Reuse of the trained Project 2 Random Forest model

## API endpoints

### GET /
Returns a basic API status message.

### GET /health
Confirms that the API and model are available.

### POST /predict
Accepts house features and returns a predicted house value.

## Docker

Build:

```bash
docker build -t house-price-api .
```

Run:

```bash
docker run -p 8000:8000 house-price-api
```

Then open:

`http://localhost:8000/docs`

## Model note

The trained model is approximately 300 MB and is intentionally kept outside the GitHub repository because of GitHub's individual file-size restriction. The application expects `house_price_model.joblib` in the same directory when run locally.
