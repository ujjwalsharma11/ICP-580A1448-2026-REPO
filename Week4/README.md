# Project 8 – Model Deployment API

This project deploys the trained Random Forest house-price model from Project 2 through a FastAPI REST API.

## Week 4
Initial API development:
- FastAPI application
- Model loading
- `/` endpoint
- `/health` endpoint
- `/predict` endpoint
- Pydantic input validation
- Automatic Swagger documentation

## Important
The trained model file `house_price_model.joblib` is about 300 MB, so it should NOT be uploaded to GitHub because GitHub's normal single-file limit is 100 MB.

Keep the model file locally beside `app.py` when running the API.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open:
`http://127.0.0.1:8000/docs`

## Prediction input order

The API expects the same 10 features used by Project 2:
MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, RoomsPerHousehold, BedroomsPerRoom.
