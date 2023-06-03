from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict

app = FastAPI()


class Input(BaseModel):
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    required_car_parking_space: int
    lead_time: int
    no_of_special_requests: int
    avg_price_per_room: float
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int


class PredictionOut(BaseModel):
    is_canceled: int


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict")
def WeatherResult(payload: Input):
    is_canceled = predict(
        payload.no_of_adults,
        payload.no_of_children,
        payload.no_of_weekend_nights,
        payload.no_of_week_nights,
        payload.required_car_parking_space,
        payload.lead_time,
        payload.no_of_special_requests,
        payload.avg_price_per_room,
        payload.repeated_guest,
        payload.no_of_previous_cancellations,
        payload.no_of_previous_bookings_not_canceled /
        (payload.no_of_previous_bookings_not_canceled + payload.no_of_previous_cancellations)
    )

    return {"Result": int(str(is_canceled))}
