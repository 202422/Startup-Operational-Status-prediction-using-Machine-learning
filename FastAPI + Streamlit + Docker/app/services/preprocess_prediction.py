import pandas as pd
import joblib
import numpy as np

def predict_process(data: dict):

    df_input = pd.DataFrame([data])

    num_feat = ['founded_at', 'active_days', 'first_funding_at', 'last_funding_at',
 'funding_total_usd', 'first_milestone_at', 'last_milestone_at', 'milestones',
 'relationships', 'lng']
    
    feat_log_transform = ["founded_at", "active_days", "first_funding_at", 
                          "funding_total_usd", "milestones", "relationships"]
    
    for col in feat_log_transform:
        df_input[col] = np.log1p(df_input[col])


    interaction_term = joblib.load("models/interaction_term.pkl")

    model = joblib.load("models/Ada_Boost_Multiclass.pkl")

    target_encoder = joblib.load("models/label_encod_Target.pkl")

    one_hot_encod = joblib.load("models/one_hot_encod.pkl")

    scaler = joblib.load("models/standard_scaler.pkl")

    scaler_df = scaler.transform(df_input[num_feat])

    df_input[num_feat] = scaler_df

    encoded_data = one_hot_encod.transform(df_input[["category_code","country_code"]])

    df_input_encod = pd.concat([df_input, encoded_data], axis = 1)

    
    poly_features = interaction_term.transform(df_input_encod[num_feat])
    df_poly = pd.DataFrame(poly_features, columns=interaction_term.get_feature_names_out(num_feat))

    df_input2 = pd.concat([df_input_encod, df_poly[['founded_at active_days','first_funding_at last_milestone_at',
    'first_funding_at funding_total_usd', 'first_milestone_at last_milestone_at']]], axis = 1)

   


    FEATURE_ORDER = [
    "founded_at", "active_days", "first_funding_at", "last_funding_at",
    "funding_total_usd", "first_milestone_at", "last_milestone_at", "milestones",
    "relationships", "lng", "founded_at active_days", "first_funding_at last_milestone_at", "first_funding_at funding_total_usd", "first_milestone_at last_milestone_at",
    "category_code_advertising", "category_code_biotech", "category_code_consulting",
    "category_code_ecommerce", "category_code_enterprise", "category_code_games_video",
    "category_code_mobile", "category_code_other", "category_code_public_relations",
    "category_code_software", "category_code_web",
    "country_code_AUS", "country_code_CAN", "country_code_DEU", "country_code_ESP",
    "country_code_FRA", "country_code_GBR", "country_code_IND", "country_code_ISR",
    "country_code_NLD", "country_code_USA", "country_code_other"
]


    df_final = df_input2[FEATURE_ORDER]

    prediction = model.predict(df_final)
    prediction_label = target_encoder.inverse_transform(prediction)[0]

    return prediction_label

