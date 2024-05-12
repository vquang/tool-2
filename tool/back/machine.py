import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from global_var import *

tfid = TfidfVectorizer(max_features=1000)
pca = PCA(256)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

def train():
    # chuẩn bị dữ liệu huấn luyện và kiểm thử---------------------------------------------
    train = pd.read_csv('payload_train.csv', header=None).values
    feature_train = [' '.join(row) for row in [row[0:2] for row in train][1:]]
    label_train = [row[2] for row in train][1:]


    # # tiền xử lý--------------------------------------------------------------------------
    # # chuyển các đặc trưng từ chuỗi sang số

    feature_train_tfid = tfid.fit_transform(feature_train)

    feature_train_pca = pca.fit_transform(feature_train_tfid.toarray())
    

    # chuyển các nhãn từ chuỗi sang số
    mapping = ['norm','sqli','xss','cmdi','path-traversal']
    label_encoder = LabelEncoder()
    label_encoder.classes_ = np.array(mapping)

    label_train_encoded = label_encoder.transform(label_train)
    #--------------------------------------------------------------------------------------

    # bắt đầu huấn luyện-------------------------------------------------------------------

    rf_classifier.fit(feature_train_pca, label_train_encoded)
    #--------------------------------------------------------------------------------------

def analyze():

# dự đoán nhãn thu được từ dữ liệu kiểm thử---------------------------------------------
    data = pd.read_csv('/home/user/log/log.csv', header=None).values
    feature_data = [row[-1] for row in data][0:]
    feature_data_tfid = tfid.transform(feature_data)
    feature_data_pca = pca.transform(feature_data_tfid.toarray())
    label_pred = rf_classifier.predict(feature_data_pca)


#---------------------------------------------------------------------------------------

# ghi những log là sql injection ra file sqli.log
    data = [' '.join(row) for row in [row[0:6] for row in data][0:]]
    for i in range(len(data)):
        if(label_pred[i] == 1):
            with open(SQLI_FILE, 'a') as file:
                file.write(f"{data[i]}\n")
        if(label_pred[i] == 2):
            with open(XSS_FILE, 'a') as file:
                file.write(f"{data[i]}\n")
        if(label_pred[i] == 3):
            with open(CMDI_FILE, 'a') as file:
                file.write(f"{data[i]}\n")
        if(label_pred[i] == 4):
            with open(PATH_TRAVERSAL, 'a') as file:
                file.write(f"{data[i]}\n")
