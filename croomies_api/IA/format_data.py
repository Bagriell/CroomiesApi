import pathlib
import pickle
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os


def predict_cluster(jsonData):
    # read data
    data_user = pd.read_json(jsonData)
    # reorder columns
    data_user.answers.age = data_user.profile.age
    data_user.drop(columns=['address', 'budget', 'date',
                'numberSeeker', 'profile'], inplace=True)
    data_user.dropna(inplace=True)
    column_names_order = ["age", "diet", "drinks", "education",
                        "speaks", "religion", "smokes", "pets"]
    data_user = data_user.transpose()
    data_user = data_user.reindex(columns=column_names_order)

    # cat & dogs encoding
    if data_user.pets[0] == "Je ne veux pas vivre avec des animaux":
        data_user['like_has_cats'] = 0
        data_user['like_has_dogs'] = 0
    elif data_user.pets[0] == "Je possède un/des chat(s)" or data_user.pets[0] == "Je veux bien vivre avec un chat":
        data_user['like_has_cats'] = 1
        data_user['like_has_dogs'] = 0
    elif data_user.pets[0] == "Je possède un/des chien(s)" or data_user.pets[0] == "Je veux bien vivre avec un chien":
        data_user['like_has_cats'] = 0
        data_user['like_has_dogs'] = 1
    elif data_user.pets[0] == "Je possède chat et chien" or data_user.pets[0] == "Je veux bien vivre avec un chien ou un chat":
        data_user['like_has_cats'] = 1
        data_user['like_has_dogs'] = 1
    elif data_user.pets[0] == "Je possède chat et chien":
        data_user['like_has_cats'] = 1
        data_user['like_has_dogs'] = 1
    else:
        return('error encoding cat & dogs !')

    data_user.drop(columns=['pets'], inplace=True)


    # Go to matrix
    
    full_pipeline = joblib.load(os.getcwd() + '/croomies_api/IA/pipeline_model.pkl')
    data_user.drop(data_user.index[1:], inplace=True)
    data_user_prepared = full_pipeline.transform(data_user)

    # TEST **********************
    # data = [{'age': 5, 'diet': 'Je mange de tout', 'drinks':"Lors d'évènements", 'education':"BTS/DUT (en cours)", 'speaks':"english", 'religion':"Bouddhiste", 'smokes':"Jamais", 'like_has_cats':1, 'like_has_dogs':1}]
    # df = pd.DataFrame(data)
    # df_prepared = full_pipeline.transform(df)

    loaded_model = pickle.load(open(os.getcwd() + '/croomies_api/IA/cluster_model.pkl', 'rb'))
    result = loaded_model.predict(data_user_prepared)
    return result