import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import f1_score, classification_report
from sklearn.pipeline import Pipeline
from tqdm import tqdm
import pickle
import plotly.express as px
import seaborn as sns
import streamlit as st

st.title=('Model Churn Prediction')

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
     #To read file as bytes:
     #bytes_data = uploaded_file.getvalue()
     #st.write(bytes_data)

    df = pd.read_csv(uploaded_file)
    st.write(df)

    customers = pd.Series(df['Customer ID'])

    selector = pickle.load(open('selected_cols_tel.pickle', 'rb'))
    scaler = pickle.load(open('scaler_tel.pickle', 'rb'))
    model = pickle.load(open('rfc_model_tel.pickle', 'rb'))
    kbset = pickle.load(open('dummy_cols_tel.pickle', 'rb'))

    #saving our customer info

    customers = pd.Series(df['Customer ID'])

    df = df.drop(['Customer ID', 'Offer'], axis=1)

    imputer=SimpleImputer(strategy = 'most_frequent')
    cols = df.columns.tolist()
    imputed_X = pd.DataFrame(imputer.fit_transform(df), columns = cols)

    int_col=df.select_dtypes(include='number')
    int_col_l=list(int_col.columns)

    imputed_X[int_col_l]=imputed_X[int_col_l].astype(float)

    #dummies

    df_enconded = pd.get_dummies(imputed_X, columns=kbset)

    #scaled

    scaled = scaler.transform(df_enconded)

    #select k best

    selector_kbest = selector.transform(scaled)

    #model prediction

    predictions = model.predict(selector_kbest)

    predictions__ = pd.Series(list(predictions))

    final_results = pd.concat([customers,predictions__], axis=1)
    final_results.rename(columns={0:'Churn Value'}, inplace=True)
    final_results_value1 = final_results[final_results['Churn Value'] == 1]
    final_results_value1 

else: 
    
    st.info("Please upload a valid file.")  