import pandas as pd
from sklearn.model_selection import train_test_split

from parameter_finder import classification_parameter_finder
from  pharameter_models.models import get_details_models

import warnings
from sklearn.exceptions import ConvergenceWarning

# Ignore ConvergenceWarning
warnings.filterwarnings("ignore", category = ConvergenceWarning)


def train_models(x_data : dict,
                 y : pd.DataFrame):
    
    details_models = get_details_models()

    results = []


    print("📌start train model ...")

    for  name_section, data_section in x_data.items():
        method = name_section

        X_train, X_test, y_train, y_test = train_test_split(data_section, y, test_size=0.2, random_state=42)

        for detail_model in details_models:
            model, parameters = detail_model

            print(f"--- 📌start train <<{model}>> on <<{method}>> data")

            _result = classification_parameter_finder(model,
                                                parameters,
                                                X_train,
                                                y_train,
                                                X_test,
                                                y_test,
                                                method)
                
            print(f"--- ✅finish train <<{model}>> on <<{method}>> data")
            results.append(_result)
            results_df = pd.concat(results, ignore_index=True)
            results_df.to_csv("./result/result.csv")



    print("✅finish train model")

    results = pd.concat(results, ignore_index=True)

    results.to_csv("./result/result.csv")

    print("             ✅save result in local path✅              ")