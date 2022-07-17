import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from seaborn import heatmap
import matplotlib.pyplot as plt
import random

#criar os gráficos das árvores de decisão
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image  
import pydotplus


def calculateDecisionTreeKfold(n_splits, shuffle, random_state, X, y):
    kfold = KFold(n_splits=14, shuffle=True, random_state=80)
    model_dtc_kfold_3_entropy = DecisionTreeClassifier(criterion="entropy")
    print(kfold.get_n_splits(X))
    # Médias
    accuracy_med_train = 0
    accuracy_med_test = 0
    count_split = 0
    for train_index, test_index in kfold.split(X):
        count_split +=1
        print(" Treino:", train_index, "Teste:", test_index)
        X_train, X_test = X.loc[train_index,:], X.loc[test_index,:]
        y_train, y_test = y[train_index], y[test_index]
        model_dtc_kfold_3_entropy.fit(X_train, y_train)
        y_pred_train = model_dtc_kfold_3_entropy.predict(X_train)
        y_pred_test = model_dtc_kfold_3_entropy.predict(X_test)
        # Cálculo das acurácias
        accuracy_train = metrics.accuracy_score(y_train, y_pred_train)
        accuracy_test = metrics.accuracy_score(y_test, y_pred_test)
        print("Iteração: " + str(count_split) + " \n" + "Acurácia do treinamento: " + str(accuracy_train) + " \n" + "Acurácia do teste: " + str(accuracy_test))
        # Cálculo das médias
        accuracy_med_train += accuracy_train/kfold.get_n_splits(X)
        accuracy_med_test += accuracy_test/kfold.get_n_splits(X)
    print("Acurácia média do treinamento:", accuracy_med_train)
    print("Acurácia média do teste:", accuracy_med_test)

