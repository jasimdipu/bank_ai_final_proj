import pickle

from .models import CustomerData
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import pickle


# fetch data
def fetch_data():
    data = CustomerData.objects.all()
    df = pd.DataFrame(data)

    return df


# clean data
def clean_data():
    data = fetch_data()
    data.dropna(axis=0, how='any', inplace=True)
    data.drop_duplicates(inplace=True)
    return data


# preprocess data
def preprocess_data():
    data = clean_data()
    encoder = OneHotEncoder()
    encoder.fit_transform(data[["personal_loan", "creditcard", "securities_account",
                                "cd_account", "online"]])
    return data


# feature eng
def feature_engineering():
    data = preprocess_data()
    x = data.drop(columns=['personal_loan'])
    y = data['personal_loan']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    return x_train_scaled, x_test_scaled, y_train, y_test


# train model
def train_model():
    x_train_scaled, x_test_scaled, y_train, y_test = feature_engineering()
    # Instantiate the Logistic Regression model
    logreg = LogisticRegression(max_iter=1000)
    # Fit the Logistic Regression model
    logreg.fit(x_train_scaled, y_train)
    # Predict the response for test data with Logistic Regression
    y_pred_logreg = logreg.predict(x_test_scaled)
    print("\nLogistic Regression Model:")
    print("Accuracy of Training data set: {0:.4f} %".format(
        accuracy_score(y_train, logreg.predict(x_train_scaled)) * 100))
    print("Accuracy of Test data set: {0:.4f} %".format(accuracy_score(y_test, y_pred_logreg) * 100))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred_logreg))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_logreg))

    # Fit the KNN model
    knn = KNeighborsClassifier(n_neighbors=3)
    # Fit the KNN model
    knn.fit(x_train_scaled, y_train)
    y_pred_knn = knn.predict(x_test_scaled)
    print("KNN Model:")
    print("Accuracy of Training data set: {0:.4f} %".format(accuracy_score(y_train, knn.predict(x_train_scaled)) * 100))
    print("Accuracy of Test data set: {0:.4f} %".format(accuracy_score(y_test, y_pred_knn) * 100))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred_knn))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_knn))

    filename1 = "loan_log.sav"
    filename2 = "loan_knn.sav"
    pickle.dump(logreg, open(filename1, "wb"))
    pickle.dump(knn, open(filename2, "wb"))
