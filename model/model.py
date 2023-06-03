from pathlib import Path
from sklearn.decomposition import PCA
import pickle

BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(f"{BASE_DIR}/model.pkl", "rb") as f1:
    clf = pickle.load(f1)


def predict(no_of_adults,
            no_of_children,
            no_of_weekend_nights,
            no_of_week_nights,
            required_car_parking_space,
            lead_time,
            no_of_special_requests,
            avg_price_per_room,
            repeated_guest,
            no_of_previous_cancellations,
            cancellations_rate
            ):

    input = [
        no_of_adults,
        no_of_children,
        no_of_weekend_nights,
        no_of_week_nights,
        required_car_parking_space,
        lead_time,
        repeated_guest,
        avg_price_per_room,
        no_of_special_requests,
        cancellations_rate
    ]
    return clf.predict([input])[0]
