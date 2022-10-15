# hier sind 2 Todos wo ihr das auf euer Zeug anpassen müsst, einfach eure Empfehlungsmethoden rein tun

[1]# Import Modules
import time
# Runtime variable
start = time.time()
import json
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from statistics import mean
# TODO: Eure prediction Methode importieren
from recommandation import get_list_of_recommendation

def get_user_ids_to_drop():
    user_ids_to_drop = []
    f = open('data/testset.json')
    data = json.load(f)
    for i in data:
        user_ids_to_drop.append(i['User_Id'])
    return user_ids_to_drop

def get_calculation_base(raw_true, raw_pred):
    boolean_true = []
    boolean_pred = []
    for i in range(17770):
        boolean_true.append(False)
        boolean_pred.append(False)
    for i in raw_true:
        boolean_true[i-1] = True
    for i in raw_pred:
        boolean_pred[int(i["recommendation"])] = True
    return boolean_true, boolean_pred

def test_if_avaible(movie):
    df_titels = pd.read_csv('data/recommendations_titles.csv', header=None, sep=';')        
    df_ids = pd.read_csv('data/recommendations_ids.csv', header=None, sep=';')
        
    try:
        df_titels.loc[df_titels[0] == movie].values      
        df_ids.loc[df_ids[0] == movie].values
    except:
        return False

def get_mean_precision_recall(): 
    # Opening JSON file
    f = open('data/testset.json')
    
    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the dictionary
    precision_total = []
    recall_total = []

    for i in data:
        #################################################################
        # TODO: An dieser Stelle müssen eure predictions eingefügt werden 
        # Get predictions for the prediction base

        raw_pred = []
        for j in i['Prediction_Base']:
            l = {j}
            if test_if_avaible(j) != False:
                raw_pred = np.append(raw_pred, get_list_of_recommendation(l))

        #################################################################
        # Get true values for the prediction base
        if raw_pred.size != 0:
            raw_true = i['Raw_true']
            for i in raw_pred:
                if i in raw_true:
                    print("Vorhanden")
                else:
                    print("Nicht vorhanden")

            # Get precision and recall for particular testdata
            boolean_true, boolean_pred = get_calculation_base(raw_true, raw_pred)
            precision = precision_score(y_true = boolean_true, y_pred = boolean_pred)
            recall = recall_score(y_true = boolean_true, y_pred = boolean_pred)
            precision_total = np.append(precision_total,precision)
            recall_total = np.append(recall_total,recall)

            print(boolean_pred)

    return mean(precision_total), mean(recall_total)

mean_precision, mean_recall = get_mean_precision_recall()
print(mean_precision)
print(mean_recall)

[8]# Runtime analysis
end = time.time()
print('Runtime: {:5.3f}s'.format(end-start))