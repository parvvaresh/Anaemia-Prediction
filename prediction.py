import joblib
import pandas as pd


def predict(data : pd.DataFrame) -> int:

    model_dt = joblib.load('my_model.pkl')
    return model_dt.predict(data)
