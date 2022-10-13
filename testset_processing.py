# hier sind 2 Todos wo ihr das auf euer Zeug anpassen müsst, einfach eure Empfehlungsmethoden rein tun

[1]# Import Modules
import time
# Runtime variable
start = time.time()
import json
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from statistics import mean
# TODO: Eure prediction Methode importieren
from RecSys2 import RecSystem

def get_user_ids_to_drop():
    user_ids_to_drop = []
    f = open('app/testset.json')
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
        boolean_pred[int(i-1)] = True
    return boolean_true, boolean_pred

def get_mean_precision_recall(): 
    # Opening JSON file
    f = open('app/testset.json')
    
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
            raw_pred = np.append(raw_pred, RecSystem(j))
        #################################################################
        # Get true values for the prediction base
        raw_true = i['Raw_true']

        # Get precision and recall for particular testdata
        boolean_true, boolean_pred = get_calculation_base(raw_true, raw_pred)
        precision = precision_score(y_true = boolean_true, y_pred = boolean_pred)
        recall = recall_score(y_true = boolean_true, y_pred = boolean_pred)
        precision_total = np.append(precision_total,precision)
        recall_total = np.append(recall_total,recall)

    return mean(precision_total), mean(recall_total)

mean_precision, mean_recall = get_mean_precision_recall()
print(mean_precision)
print(mean_recall)

[8]# Runtime analysis
end = time.time()
print('Runtime: {:5.3f}s'.format(end-start))