import joblib
import pandas as pd


def predict(data : pd.DataFrame) -> int:

    model_dt = joblib.load('./model/fainal_model/dt.pkl')
    return model_dt.predict(data)
